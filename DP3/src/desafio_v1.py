import textwrap

saldo = 0
extrato = []
usuarios = []
contas_correntes = []
saques_diarios = 0
limite_saques = 3
limite = 500

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("\n@@@ CPF já cadastrado. Não é possível cadastrar o usuário. @@@")
            return

    # Cria um dicionário com os dados do usuário
    usuario = {
        'cpf': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,        
        'endereco': endereco
    }

    # Adiciona o usuário à lista de usuários
    usuarios.append(usuario)

    print("\n=== Usuário cadastrado com sucesso! ===")

def cadastrar_conta_corrente(cpf_usuario):
    
    # Verifica se o usuário com o CPF informado existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("\n@@@ Usuário não encontrado. Não é possível cadastrar a conta corrente. @@@")
        return

    # Gera o número da conta sequencialmente
    numero_conta = len(contas_correntes) + 1

    # Cria um dicionário com os dados da conta corrente
    conta_corrente = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    }

    # Adiciona a conta corrente à lista de contas correntes
    contas_correntes.append(conta_corrente)

    print("\n=== Conta corrente cadastrada com sucesso! ===")

def deposito(saldo, valor, extrato):
        
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"=== Depósito de R$ {valor:.2f} realizado com sucesso.===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def saque(*,saldo, valor,saques_diarios, extrato,limite=500, limite_saques=3):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = saques_diarios >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:        
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_diarios += 1              
            
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        
    else:
        print(print("\n@@@ Operação falhou! O valor informado é inválido. @@@"))    

    return saldo, extrato, saques_diarios
    

def extrat(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:        
        for movimentacao in extrato:
            print(movimentacao)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================")      


def listar_contas():
    
    if not contas_correntes:
        print("\n@@@ Não há contas correntes cadastradas. @@@")
    else:
        print("Contas Correntes:")
        for conta_corrente in contas_correntes:
            numero_conta = conta_corrente['numero_conta']
            agencia = conta_corrente['agencia']
            usuario = conta_corrente['usuario']
            print(f"Conta: {agencia} - {numero_conta} (CPF: {usuario['cpf']}, Nome: {usuario['nome']})")

def listar_usuarios():
    
    if not usuarios:
        print("\n@@@ Não há usuários cadastrados. @@@")
    else:
        print("Usuários:")
        for usuario in usuarios:
            print(f"CPF: {usuario['cpf']}, Nome: {usuario['nome']}")

# Função para exibir o menu
def exibir_menu():
    menu = """\n
    ================ MENU ================    
    [cu]\tCadastrar Usuário
    [lu]\tListar Usuários
    [cc]\tCadastrar Conta Corrente
    [lc]\tListar Contas
    [d ]\tDepositar
    [s ]\tSacar
    [e ]\tExtrato
    [q ]\tSair
    => """
    return input(menu).lower().strip()

# Função Principal

def main():
    while True:
        opcao = exibir_menu()
        global saldo, extrato, saques_diarios
        
        if  opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))            
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, saques_diarios = saque(saldo=saldo, valor=valor, extrato=extrato, saques_diarios=saques_diarios)
        elif opcao == "e":
            extrat(saldo, extrato=extrato)
        elif opcao == "lc":
            listar_contas()
        elif opcao == "lu":
            listar_usuarios()
        elif opcao == "cu":
            cpf = int(input("Informe o CPF (somente número): "))
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "cc":
            cpf_usuario = int(input("Digite o CPF do usuário proprietário da conta: "))
            cadastrar_conta_corrente(cpf_usuario)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    main()    