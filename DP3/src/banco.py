# Importando bibliotecas necessárias
import datetime
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Declarando a base para criação de classes ORM
Base = declarative_base()

# Definindo a classe de modelo para usuários
class Usuario(Base):
    __tablename__ = 'usuarios'

    cpf = Column(String, primary_key=True)
    nome = Column(String)
    data_nascimento = Column(String)
    endereco = Column(String)

# Definindo a classe de modelo para contas correntes
class ContaCorrente(Base):
    __tablename__ = 'contas_correntes'

    numero_conta = Column(Integer, primary_key=True, autoincrement=True)
    agencia = Column(String, default='0001')  # Agência preenchida automaticamente
    cpf_usuario = Column(String, ForeignKey('usuarios.cpf'))
    saldo = Column(Float)
    limite = Column(Integer)

    # Construtor da classe
    def __init__(self, cpf_usuario, saldo=0, limite=3):
        self.cpf_usuario = cpf_usuario
        self.saldo = saldo
        self.limite = limite
        self.movimentacoes = []

# Definindo a classe de modelo para movimentações
class Movimentacao(Base):
    __tablename__ = 'movimentacoes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_conta = Column(Integer, ForeignKey('contas_correntes.numero_conta'))
    tipo = Column(String)
    valor = Column(Float)
    data_hora = Column(String)

# Definindo a classe de modelo para saques diários
class SaqueDiario(Base):
    __tablename__ = 'saques_diarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_conta = Column(Integer, ForeignKey('contas_correntes.numero_conta'))
    data = Column(String)
    quantidade = Column(Integer)

# Classe principal do banco
class Banco:
    def __init__(self):
        # Criando conexão com o banco de dados SQLite
        self.engine = create_engine('sqlite:///database/banco.db')
        # Criando as tabelas no banco de dados
        Base.metadata.create_all(self.engine)
        # Criando a sessão para interagir com o banco de dados
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # Método para criar um novo usuário
    def criar_usuario(self):
        cpf = input("CPF (11 caracteres): ")
        if len(cpf) != 11:
            print("CPF deve ter 11 caracteres.")
            return

        usuario = self.session.query(Usuario).filter_by(cpf=cpf).first()

        if usuario:
            print("Usuário com esse CPF já existe.")
        else:
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
            
            novo_usuario = Usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
            self.session.add(novo_usuario)
            self.session.commit()
            print("Usuário cadastrado com sucesso.")

    # Método para criar uma nova conta corrente
    def criar_conta_corrente(self):
        cpf = input("CPF do usuário: ")
        usuario = self.session.query(Usuario).filter_by(cpf=cpf).first()

        if usuario:
            nova_conta = ContaCorrente(cpf_usuario=cpf)
            self.session.add(nova_conta)
            self.session.commit()
            print("Conta corrente criada com sucesso.")
        else:
            print("Usuário não encontrado.")

    # Método para listar todas as contas correntes
    def listar_contas(self):
        contas = self.session.query(ContaCorrente).all()
        print("=== LISTA DE CONTAS ===")
        for conta in contas:
            print(f"Agência: {conta.agencia}")
            print(f"Número da conta: {conta.numero_conta}")
            print(f"CPF do titular: {conta.cpf_usuario}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
            print(f"Limite: {conta.limite} saques diários")
            print("=" * 20)

    # Método para listar todos os usuários
    def listar_usuarios(self):
        usuarios = self.session.query(Usuario).all()
        print("=== LISTA DE USUÁRIOS ===")
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}")
            print(f"CPF: {usuario.cpf}")
            print("=" * 20)

    # Método para buscar um usuário pelo CPF
    def buscar_usuario(self, cpf):
        usuario = self.session.query(Usuario).filter_by(cpf=cpf).first()
        if usuario:
            return usuario
        else:
            return None

    # Método para realizar movimentações (depósito ou saque) em uma conta corrente
    def realizar_movimentacao(self, conta_corrente, tipo, valor):
        if tipo not in ["Depósito", "Saque"]:
            print("Tipo de movimentação inválido.")
            return

        if tipo == "Saque":
            hoje = datetime.date.today()
            saque_diario = self.session.query(SaqueDiario).filter_by(numero_conta=conta_corrente.numero_conta, data=str(hoje)).first()

            if saque_diario:
                if saque_diario.quantidade >= conta_corrente.limite:
                    print("Limite máximo de saques diários atingido.")
                    return
                else:
                    saque_diario.quantidade += 1
            else:
                saque_diario = SaqueDiario(numero_conta=conta_corrente.numero_conta, data=str(hoje), quantidade=1)
                self.session.add(saque_diario)

        movimentacao = Movimentacao(numero_conta=conta_corrente.numero_conta, tipo=tipo, valor=valor, data_hora=str(datetime.datetime.now()))
        if tipo == "Depósito":
            conta_corrente.saldo += valor
        elif tipo == "Saque":
            conta_corrente.saldo -= valor

        self.session.add(movimentacao)
        self.session.commit()
        print(f"{tipo} de R$ {valor:.2f} realizado com sucesso.")

    # Método para visualizar o extrato de uma conta corrente
    def extrato(self, conta_corrente):
        print("Extrato:")
        usuario = self.session.query(Usuario).filter_by(cpf=conta_corrente.cpf_usuario).first()
        print(f"========= Conta:{conta_corrente.numero_conta} - Usuário: {usuario.nome} ==========")

        movimentacoes = self.session.query(Movimentacao).filter_by(numero_conta=conta_corrente.numero_conta).all()
        total = 0

        for movimentacao in movimentacoes:
            data_hora = datetime.datetime.strptime(movimentacao.data_hora, "%Y-%m-%d %H:%M:%S.%f")
            tipo = movimentacao.tipo
            valor = movimentacao.valor
            if tipo == "Depósito":
                total += valor
            elif tipo == "Saque":
                total -= valor

            print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {valor:.2f}")

        print(f"\n-------------------------- Total: R$ {total:.2f}")
        print('=' * 45)

    # Método para fechar a conexão com o banco de dados
    def fechar_conexao(self):
        self.session.close()
        print("Sessão encerrada com sucesso!")

# Função para exibir o menu principal
def exibir_menu():
    menu = """
    [1] Criar usuário
    [2] Criar conta corrente
    [3] Listar contas
    [4] Listar usuários
    [5] Acessar conta    
    [q] Sair
    => """
    return input(menu).lower().strip()

# Função para exibir o menu das operações de conta
def exibir_menu_conta():
    menu = """
    [d] Depósito
    [s] Saque
    [e] Extrato       
    [q] Sair
    => """
    return input(menu).lower().strip()

# Função principal para executar o programa
def main():
    banco = Banco()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            banco.criar_usuario()
        elif opcao == "2":
            banco.criar_conta_corrente()
        elif opcao == "3":
            banco.listar_contas()
        elif opcao == "4":
            banco.listar_usuarios()
        elif opcao == "5":
            cpf = input("CPF do titular da conta: ")
            usuario = banco.buscar_usuario(cpf)

            if not usuario:
                print("Usuário não encontrado.")
                continue

            contas_usuario = banco.session.query(ContaCorrente).filter_by(cpf_usuario=cpf).all()

            if not contas_usuario:
                print("O usuário não possui contas correntes.")
                continue

            print(f"Contas correntes do usuário ({usuario.nome}):")
            for conta in contas_usuario:
                print(f"Agência: {conta.agencia}")
                print(f"Número da conta: {conta.numero_conta}")
                print("=" * 20)

            numero_conta = int(input("Número da conta: "))
            conta_corrente = banco.session.query(ContaCorrente).filter_by(numero_conta=numero_conta).first()

            if conta_corrente and conta_corrente.cpf_usuario == cpf:
                while True:
                    opcao_conta = exibir_menu_conta()

                    if opcao_conta == "d":
                        try:
                            valor = float(input("Digite o valor a ser depositado: "))
                            banco.realizar_movimentacao(conta_corrente, "Depósito", valor)
                        except ValueError:
                            print("Valor inválido. Tente novamente.")

                    elif opcao_conta == "s":
                        try:
                            valor = float(input("Digite o valor a ser sacado: "))
                            banco.realizar_movimentacao(conta_corrente, "Saque", valor)
                        except ValueError:
                            print("Valor inválido. Tente novamente.")

                    elif opcao_conta == "e":                        
                        banco.extrato(conta_corrente)                        

                    elif opcao_conta == "q":
                        break
            else:
                print("Conta corrente não encontrada ou não pertence ao usuário.")        

        elif opcao == "q":
            print("Saindo...")
            banco.fechar_conexao()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
