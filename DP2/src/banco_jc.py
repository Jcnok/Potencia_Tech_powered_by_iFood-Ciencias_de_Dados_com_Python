import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = {}

    def deposito(self, valor):
        """
        Realiza um depósito na conta bancária.

        Args:
            valor (float): Valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        """
        Realiza um saque na conta bancária.

        Args:
            valor (float): Valor a ser sacado.
        """
        hoje = datetime.date.today()

        if hoje in self.saques_diarios and self.saques_diarios[hoje] >= 3:
            print("Limite máximo de saques diários atingido.")
            return

        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                if hoje in self.saques_diarios:
                    self.saques_diarios[hoje] += 1
                else:
                    self.saques_diarios[hoje] = 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        """Exibe o extrato da conta bancária."""
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
