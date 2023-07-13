# Desafio - Criando um sistema bancário simples.

<img src="img/personal_bank.jpg" referrerpolicy="same-origin" style="display: block; object-fit: cover; border-radius: 0px; width: 100%; height: 30vh; opacity: 1; object-position: center 50%;">

## Objetivo Geral

**Criar um sistema bancário com as operações: sacar, depositar
e visualizar extrato.**

## Desafio:

**Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a
primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.**

### Operação de depósito:

* **Deve ser possível depositar valores positivos para a minha
conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisamos nos preocupar em identificar qual
é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na
operação de extrato.**

### Operação de saque:

* **O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem
informando que não será possível sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em uma
variável e exibidos na operação de extrato.**

### Operação de extrato:

* **Essa operação deve listar todos os depósitos e saques
realizados na conta. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a
mensagem: Não foram realizadas movimentações.**
* **Os valores devem ser exibidos utilizando o formato R$ xxx.xx.**

exemplo:
1500.45 = R$ 1500.45
## Resolução #1- Código Baseado em funções

### Documentação:

**Este código implementa um sistema bancário básico em Python. Aqui estão as principais funções e seus respectivos comportamentos:**

1. **deposito(valor):**
    * Realiza um depósito na conta bancária. O parâmetro valor representa o valor a ser depositado. Se o valor for maior que zero, ele é adicionado ao saldo da conta, registrado na lista de depósitos e uma mensagem de sucesso é exibida. Caso contrário, é exibida uma mensagem informando que o valor do depósito deve ser positivo.

2. **saque(valor):**
    * Realiza um saque na conta bancária. O parâmetro valor representa o valor a ser sacado. Antes de realizar o saque, é verificado se o valor é maior que zero e se o limite máximo de saques diários (3 saques por dia) ainda não foi atingido. Em seguida, é verificado se o saldo é suficiente para realizar o saque. Se todas as condições forem atendidas, o valor é subtraído do saldo, registrado na lista de saques e atualizado o dicionário de saques diários. Caso contrário, são exibidas mensagens apropriadas informando a impossibilidade de realizar o saque.

3. **extrato():**
    * Exibe o extrato da conta bancária. Se não foram realizadas movimentações (nem depósitos nem saques), é exibida a mensagem "Não foram realizadas movimentações". Caso contrário, são exibidos os valores dos depósitos e saques realizados, seguidos pelo saldo atual.

4. **exibir_menu():**
    * Função auxiliar que exibe um menu de opções ao usuário. O usuário pode escolher entre depositar, sacar, exibir o extrato ou sair do programa. A opção escolhida é retornada como um valor de texto em minúsculo.

5. **main():**
    * Função principal que inicia a execução do programa. Um loop infinito é iniciado, onde o menu é exibido e a opção escolhida pelo usuário é processada. Dentro do loop, as funções deposito(), saque() e extrato() são chamadas de acordo com a opção selecionada pelo usuário. O loop só é interrompido quando o usuário escolhe a opção "q" para sair.
    * O código utiliza variáveis globais para manter o saldo da conta, as listas de depósitos e saques, e o dicionário de saques diários. Essas variáveis são acessadas e modificadas pelas funções do código.
    * O código utiliza a biblioteca datetime para obter a data atual e controlar o número de saques diários. As datas são usadas como chaves do dicionário saques_diarios, que armazena o número de saques realizados em cada dia.
    * O código segue boas práticas de documentação, com docstrings explicando o propósito e os parâmetros das funções. Além disso, comentários são utilizados em alguns trechos para fornecer informações adicionais.
    * A função main() é responsável por iniciar a execução do programa. Dentro dessa função, o loop principal é implementado e as opções do menu são processadas.
    * Para utilizar o programa, o usuário deve executar o código. Em seguida, é exibido um menu com as opções disponíveis. O usuário pode escolher uma opção digitando a letra correspondente e pressionando Enter. O programa então solicita os valores necessários para cada operação e exibe as mensagens de feedback adequadas.
    * O código permite ao usuário interagir com a conta bancária, realizando depósitos, saques, exibindo o extrato e finalizando a execução do programa.

### Código python:


```python
import datetime

saldo = 0
depositos = []
saques = []
saques_diarios = {}

def deposito(valor):
    """
    Realiza um depósito na conta bancária.
    
    Args:
        valor (float): Valor a ser depositado.
    """
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

def saque(valor):
    """
    Realiza um saque na conta bancária.
    
    Args:
        valor (float): Valor a ser sacado.
    """
    global saldo
    if valor > 0:
        hoje = datetime.date.today()
        
        # Verifica se já foram realizados 3 saques hoje
        if hoje in saques_diarios and saques_diarios[hoje] >= 3:
            print("Limite máximo de saques diários atingido.")
            return
        
        # Verifica se o saldo é suficiente para realizar o saque
        if saldo >= valor:
            saldo -= valor
            saques.append(valor)
            
            # Atualiza o dicionário de saques diários
            if hoje in saques_diarios:
                saques_diarios[hoje] += 1
            else:
                saques_diarios[hoje] = 1
            
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("O valor do saque deve ser positivo.")

def extrato():
    """Exibe o extrato da conta bancária."""
    global saldo
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        
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
    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            deposito(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saque(valor)
        elif opcao == "e":
            extrato()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

```

    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => d
    Digite o valor a ser depositado: 100
    Depósito de R$ 100.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 200
    Saldo insuficiente para realizar o saque.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 20
    Saque de R$ 20.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 10
    Saque de R$ 10.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => e
    Extrato:
    Depósito: R$ 100.00
    Saque: R$ 20.00
    Saque: R$ 10.00
    Saldo atual: R$ 70.00
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => q
    Saindo...
    

## Resolução #2 - Código Baseado em POO

### Documentação:

**Este código implementa um sistema bancário básico em Python usando a classe Banco. Aqui estão as principais informações sobre a classe e suas funções:**

1. **Banco:**
    **Classe que representa um banco e suas operações básicas.**

    * **Atributos:**
        * **saldo**(float): Saldo atual da conta bancária.
        * **depositos**(list): Lista de depósitos realizados na conta.
        * **saques**(list): Lista de saques realizados na conta.
        * **saques_diarios**(dict): Dicionário com o número de saques diários realizados.
        
    * **Métodos:**
        * **deposito(valor)**:Realiza um depósito na conta bancária.
        * **saque(valor)**:Realiza um saque na conta bancária.
        * **extrato()**:Exibe o extrato da conta bancária.

2. **deposito(valor):**
    * **parâmetro: valor(float):** Valor a ser depositado.
    
    * Se o valor fornecido for maior que zero, ele é adicionado ao saldo da conta, registrado na lista de depósitos e uma mensagem de sucesso é exibida. Caso contrário, é exibida uma mensagem informando que o valor do depósito deve ser positivo.
    
3. **saque(valor):**
    * **parâmetro: valor(float)** - Valor a ser sacado.
    * Antes de realizar o saque, é verificado se a quantidade de saques diários não ultrapassou o limite máximo de 3 saques por dia. Em seguida, é verificado se o valor fornecido é maior que zero e se o saldo da conta é suficiente para realizar o saque. Se todas as condições forem atendidas, o valor é subtraído do saldo, registrado na lista de saques e atualizado o dicionário de saques diários. Caso contrário, são exibidas mensagens apropriadas informando a impossibilidade de realizar o saque.

4. **extrato():**
    * **Exibe o extrato da conta bancária.**
    * Se não foram realizadas movimentações (nem depósitos nem saques), é exibida a mensagem "Não foram realizadas movimentações". Caso contrário, são exibidos os valores dos depósitos e saques realizados, seguidos pelo saldo atual da conta.
    
5. **exibir_menu():**
    * **Função que exibe o menu de opções para o usuário.**
    * Retorno:
        * **str:** Opção selecionada pelo usuário.
        * A função exibe um menu com opções de depósito, saque, extrato e sair. O usuário deve escolher uma opção digitando a letra correspondente e pressionando Enter. A opção selecionada é retornada como uma string em minúsculo.

6. **main():**
    * **Função principal que inicia a execução do programa.**
    * A função cria uma instância da classe Banco e entra em um loop infinito. Dentro do loop, exibe o menu, processa a opção selecionada pelo usuário e chama os métodos apropriados da instância de Banco. O loop é interrompido quando o usuário seleciona a opção de sair.
    
**O código segue boas práticas de documentação, com docstrings explicando o propósito, os parâmetros e os retornos das funções. Também é utilizado um bloco if __name__ == "__main__" para permitir a execução do programa quando o arquivo é executado diretamente.**

**Para utilizar o programa, o usuário deve executar o código. Será exibido um menu com opções, onde o usuário pode escolher entre depositar, sacar, exibir o extrato ou sair do programa. O programa solicitará os valores necessários para cada operação e exibirá as mensagens de feedback apropriadas. O usuário pode interagir com a conta bancária enquanto o programa estiver em execução.**

### Código Python:


```python
import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = {}

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
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
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

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
```

    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => d
    Digite o valor a ser depositado: 5000
    Depósito de R$ 5000.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 1000
    Saque de R$ 1000.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 300
    Saque de R$ 300.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 2000
    Saque de R$ 2000.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 100
    Limite máximo de saques diários atingido.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => e
    Extrato:
    Depósito: R$ 5000.00
    Saque: R$ 1000.00
    Saque: R$ 300.00
    Saque: R$ 2000.00
    Saldo atual: R$ 1700.00
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => q
    Saindo...
    

## Formas de reutilizar o código.

**Com a POO, é mais fácil reutilizar o código, já que as classes e objetos podem ser utilizados em diferentes partes do programa. As classes podem ser estendidas por meio da herança, permitindo criar novas classes com base em outras já existentes, herdando seus atributos e comportamentos. Isso economiza tempo e esforço na implementação de funcionalidades semelhantes em diferentes partes do código.**

### Salvei o código  abaixo como banco_jc.py na pasta src.


```python
import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = {}  # Dicionário para armazenar os saques por dia

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0:
            hoje = datetime.date.today()  # Obtemos a data atual

            # Verificamos se já foram realizados 3 saques hoje
            if hoje in self.saques_diarios and self.saques_diarios[hoje] >= 3:
                print("Limite máximo de saques diários atingido.")
                return

            # Verificamos se o saldo é suficiente para realizar o saque
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)

                # Verificamos se a data já está registrada nos saques diários
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
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

```

### Salvei o código  abaixo como desafio.py na pasta src.


```python
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
```

**observe que assim podemo importar facilmente o arquivo banco_jc.py como um lib e reutilizá-lo em outros projetos**.

* **Agora vamos importar o arquivo como uma biblioteca e fazer alguns testes**


```python
import os
```


```python
# Diretório atual
print("Diretório atual:", os.getcwd())
```

    Diretório atual: E:\meugithub\Potencia_Tech_powered_by_iFood-Ciencias_de_Dados_com_Python\DP2
    


```python
# Mudar para um diretório específico
novo_diretorio = "\meugithub\Potencia_Tech_powered_by_iFood-Ciencias_de_Dados_com_Python\DP2\src"
os.chdir(novo_diretorio)
```


```python
# Diretório atual agora é a pasta src
print("Diretório atual:", os.getcwd())
```

    Diretório atual: E:\meugithub\Potencia_Tech_powered_by_iFood-Ciencias_de_Dados_com_Python\DP2\src
    


```python
from banco_jc import Banco
```


```python
# Exemplo de uso:
banco_jc = Banco()

banco_jc.deposito(1000.50)
banco_jc.saque(500.25)
banco_jc.saque(200)
banco_jc.deposito(750.75)
banco_jc.saque(300)
banco_jc.deposito(1500)
banco_jc.extrato()

```

    Depósito de R$ 1000.50 realizado com sucesso.
    Saque de R$ 500.25 realizado com sucesso.
    Saque de R$ 200.00 realizado com sucesso.
    Depósito de R$ 750.75 realizado com sucesso.
    Saque de R$ 300.00 realizado com sucesso.
    Depósito de R$ 1500.00 realizado com sucesso.
    Extrato:
    Depósito: R$ 1000.50
    Depósito: R$ 750.75
    Depósito: R$ 1500.00
    Saque: R$ 500.25
    Saque: R$ 200.00
    Saque: R$ 300.00
    Saldo atual: R$ 2251.00
    

**Veja com uma simples importação conseguimos instanciar a classe banco**.

* **Implementando um menu:**


```python
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

```

**Vamos realizar alguns testes**:


```python
main()
```

    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => e
    Não foram realizadas movimentações.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => d
    Digite o valor a ser depositado: 2000
    Depósito de R$ 2000.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => s
    Digite o valor a ser sacado: 200
    Saque de R$ 200.00 realizado com sucesso.
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => e
    Extrato:
    Depósito: R$ 2000.00
    Saque: R$ 200.00
    Saldo atual: R$ 1800.00
    
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    
        => q
    Saindo...
    

## Conclusão:

**Neste desafio, implementamos um sistema básico que oferece as funcionalidades de depósito, saque e extrato.**

**Ao longo do desafio, exploramos diferentes abordagens, incluindo a programação orientada a objetos e o uso de funções. Ambas as abordagens têm suas vantagens e podem ser escolhidas de acordo com as necessidades do projeto.**

**No código baseado em classes, utilizamos a classe Banco para encapsular as operações bancárias e o estado da conta. Isso nos permitiu criar instâncias dessa classe e realizar operações específicas em cada objeto.**

**Já no código baseado em funções, mantivemos variáveis globais e definimos funções independentes para cada operação bancária. Essa abordagem pode ser mais adequada para casos mais simples ou quando não é necessário manter o estado em objetos.**

**Independentemente da abordagem escolhida, foi possível criar um sistema funcional que atendeu aos requisitos do banco. Implementamos a lógica para realizar depósitos, saques e exibir o extrato, levando em consideração limites diários de saques e validando os valores inseridos.**

**Ao concluir o desafio, aprendemos sobre a importância da organização do código, modularidade, encapsulamento de dados e reutilização de código. Além disso, exploramos o uso de estruturas de controle, como loops e condicionais, para criar uma interface interativa com o usuário.**

**No geral, o desafio nos permitiu aplicar nossos conhecimentos em Python e demonstrar a capacidade de desenvolver soluções modernas para atender às necessidades de um banco.**


```python

```
