# Importando banco_jc.py
from banco_jc import Banco

# Função para exibir o menu
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu).lower().strip()

# Função principal
def main():
    banco = Banco()

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            banco.deposito(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            banco.saque(valor)
        elif opcao == "e":
            banco.extrato()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()