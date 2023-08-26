import pytest
import datetime
from banco import Banco, Usuario, ContaCorrente, SaqueDiario
# variáveis globais.
cpf="12345678888"
nome="Julio Cesar Okuda"
data_nascimento = "11-06-1979"
endereco= "Av. autódromo, 400 - Interlagos - São Paulo/SP"
# Crie uma instância do banco
banco = Banco()

def test_criar_usuario_automaticamente(monkeypatch):
    # variáveis
    global cpf, nome, data_nascimento, endereco
    
    # Criação do mock de input para simular a entrada do CPF
    def mock_input(prompt):
        if prompt == "CPF (11 caracteres): ":
            return cpf
        if prompt == "Nome completo: ":
            return nome
        if prompt == "Data de nascimento (dd-mm-aaaa): ":
            return data_nascimento
        if prompt == "Endereço (logradouro, nro - bairro - cidade/sigla do estado): ":
            return endereco
    monkeypatch.setattr("builtins.input", mock_input) 
    
    # Chamada da função criar_usuario    
    banco.criar_usuario()
    
    # Busca o usuário criado no banco
    usuario_criado = banco.buscar_usuario(cpf)
    
    # Verificações
    assert usuario_criado is not None
    assert usuario_criado.cpf == cpf

def test_criar_conta_automaticamente(monkeypatch):
    # Criação do mock de input para simular a entrada do CPF
    global cpf
    def mock_input(prompt):
        if prompt == "CPF do usuário: ":
            return cpf
    monkeypatch.setattr("builtins.input", mock_input)
    
    # Chamada da função criar_conta_corrente
    banco.criar_conta_corrente()      
    
def test_listar_contas():
    # Execute o método para listar as contas
    banco.listar_contas()   

def test_listar_usuarios():
    # Execute o método para listar os usuários
    banco.listar_usuarios()
    
# função para acessar a conta e realizar movimentações
def test_movimentacoes():
    # Consulta SQLAlchemy para buscar o último item de forma descendente.       
    conta_criada = banco.session.query(ContaCorrente).filter_by(cpf_usuario=cpf).order_by(ContaCorrente.numero_conta.desc()).first()    
    numero_conta = conta_criada.numero_conta
    conta_corrente = banco.session.query(ContaCorrente).filter_by(numero_conta=numero_conta).first()
    
    # Realize um depósito de R$ 2000
    valor_deposito = 2000
    banco.realizar_movimentacao(conta_corrente, "Depósito", valor_deposito)   

    # Execute três saques de R$ 150 cada
    valor_saque = 150
    for _ in range(4):
        banco.realizar_movimentacao(conta_corrente, "Saque", valor_saque)
        
def test_extrato():
    # Consulta SQLAlchemy para buscar o último item de forma descendente.
    conta_criada = banco.session.query(ContaCorrente).filter_by(cpf_usuario=cpf).order_by(ContaCorrente.numero_conta.desc()).first()    
    numero_conta = conta_criada.numero_conta    
    conta_corrente = banco.session.query(ContaCorrente).filter_by(numero_conta=numero_conta).first()
    banco.extrato(conta_corrente) 

#Finaliza o programa
def test_finalizar_programa():    
    assert banco.fechar_conexao() is None

if __name__ == "__main__":    
    # Executar o pytest e gerar o relatório HTML
    pytest.main(["-rA", "--html=report.html", "--self-contained-html"])