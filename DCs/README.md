# Resolução dos desafios de Código Python.

<img src="./img/python.jpg" referrerpolicy="same-origin" style="display: block; object-fit: cover; border-radius: 0px; width: 100%; height: 30vh; opacity: 1; object-position: center 50%;">

<a name="ancora"></a>

# Desafios:

1. [Tempo Estimado de Entrega](#ancora1)
2. [Organizando seus Ativos](#ancora2)
3. [Ganhe uma Sobremesa Especial!](#ancora3)
4. [Gerenciamento de Pedidos de Comida Online](#ancora4)   
5. [Identificando Pedidos Veganos](#ancora5)  

<a name="ancora"></a>

<a id="ancora1"></a>
## Desafio: Tempo Estimado de Entrega

### Desafio
Imagine que você está criando um aplicativo de entrega de comida e precisa informar ao usuário o tempo estimado de entrega de um restaurante. A mensagem deve conter o nome do restaurante e o tempo estimado de entrega em minutos.

### Entrada
- A entrada deverá receber os valores abaixo:

  - nomeRestaurante (string): o nome do restaurante desejado.
  - tempoEstimadoEntrega (number): o tempo estimado de entrega em minutos.
  
### Saída
- Deverá retornar uma mensagem (string) informando ao usuário o tempo estimado de entrega do restaurante. Por exemplo, para o restaurante Bar do Zinho com o tempo estimado de entrega sendo 20, imprima:
'O restaurante Bar do Zinho entrega em 20 minutos.'

### Desafio Bônus: 
Utilize interpolação de strings para formatar sua saída ao invés da concatenação de strings tradicional.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
McDonalds   |
10          | O restaurante McDonalds entrega em 10 minutos.
----------- | ---------------------------------
KFC         |
25          | O restaurante KFC entrega em 25 minutos.
----------- | ---------------------------------
Burger King | 
5           | O restaurante Burguer King entrega em 5 minutos.
5

### Código:


```python
nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")
```

    McDonalds
    10
    O restaurante McDonalds entrega em 10 minutos.
    

[voltar](#ancora)

<a id="ancora2"></a>
## Desafio: Calcular o Preço Final de um Pedido

### Desafio
Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

### Entrada:
- A entrada deve receber os valores abaixo:

   - valorHamburguer: o valor unitário de um hambúrguer.
   - quantidadeHamburguer: a quantidade de hambúrgueres que o usuário deseja.
   - valorBebida: o valor unitário de uma bebida.
   - quantidadeBebida: a quantidade de bebidas que o usuário deseja.
   - valorPago: o valor pago pelo usuário.

### Saída:
- A saída deve retornar um texto informando o valor total do pedido e a quantidade de troco que será necessário. Por exemplo, se tivermos os seguintes valores de entrada:

    - valorHamburguer = 10.00;
    - quantidadeHamburguer = 2;
    - valorBebida = 5.00;
    - quantidadeBebida = 1;
    - valorPago = 30.00;
- De acordo com esses valores de entrada, o cálculo do preço final do pedido ficaria assim:

    - Valor total dos hambúrgueres: 10.00 * 2 = 20.00
    - Valor total da bebida: 5.00 * 1 = 5.00
    - Preço total do pedido: 20.00 + 5.00 = 25.00
    - Troco necessário: 30.00 - 25.00 = 5.00
    
- Como o usuário pagou 30.00 e o preço total do pedido ficou em 25.00 o troco necessário é de 5.00. Portanto, a saída esperada para esse exemplo seria:

    - O preço final do pedido é R\$ 25.00. Seu troco é R\\$ 5.00.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
10.00  | 
2      |
5.00   | O preço final do pedido é R\$ 25.00. Seu troco é R\\$ 5.00.
1      |
30.00  |
-----  | ---------------------------------
15.00  |  
3      | 
6.00   | O preço final do pedido é R\$ 57.00. Seu troco é R\\$ 3.00.
2      |
60.00  |
-----  | ---------------------------------
8.00   | 
1      | 
4.00   | O preço final do pedido é R\$ 24.00. Seu troco é R\\$ 30.00.
4      |
50.00  |

### Código:


```python
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoHamburguer = valorHamburguer * quantidadeHamburguer
precoBebida = valorBebida * quantidadeBebida
precoTotal = precoHamburguer + precoBebida
troco = valorPago - precoTotal

mensagem = f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}."
print(mensagem)
```

    10
    2
    5.00
    1
    30.00
    O preço final do pedido é R$ 25.00. Seu troco é R$ 5.00.
    

[voltar](#ancora)

<a id="ancora3"></a>
## Desafio: Ganhe uma Sobremesa Especial!

### Desafio
Crie um programa que informe ao usuário se ele pode receber um brinde especial de acordo com o valor total do pedido. Se o valor total do pedido for maior ou igual a R\$ 50.00, o usuário receberá uma sobremesa grátis. Caso contrário, o usuário não receberá nenhum brinde.

### Entrada
- A entrada deverá receber o valor total do pedido em uma variável numérica:
    - valorPedido: o valor do pedido.

### Saída
- Deverá retornar uma mensagem (string) que informa se o usuário ganhou uma sobremesa ou não:

   - Se valorPedido >= 50, a mensagem deve ser:
   - Parabens, você ganhou uma sobremesa gratis!
   - Caso contrário, a mensagem deve ser:
   - Que pena, você nao ganhou nenhum brinde especial.

### Desafio Bônus: 
- Utilize interpolação de strings para formatar sua saída ao invés da concatenação de strings tradicional.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
60    | Parabens, você ganhou uma sobremesa gratis!
----- | ---------------------------------
30    | Que pena, você nao ganhou nenhum brinde especial.
----- | ---------------------------------
90    | Parabens, você ganhou uma sobremesa gratis!

### Código:


```python
valorPedido = int(input())


if valorPedido >= 50:
    mensagem = "Parabens, você ganhou uma sobremesa gratis!"
else:
    mensagem = "Que pena, você nao ganhou nenhum brinde especial."

print(mensagem)
```

    60
    Parabens, você ganhou uma sobremesa gratis!
    

[voltar](#ancora)

<a id="ancora4"></a>
## Desafio: Gerenciamento de Pedidos de Comida Online

### Desafio
Você foi contratado para desenvolver um sistema que armazena informações dos pedidos de comida online realizados por um cliente. O sistema deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) e exibir o valor total de todos os pedidos realizados até o momento, com o desconto aplicado.

### Entrada
- A entrada é composta por:

    - Uma linha com um número inteiro n representando a quantidade de pedidos que o usuário deseja inserir;
    - n linhas, cada uma contendo uma string com o nome do pedido e um valor em ponto flutuante separados por espaço. O nome do pedido não contém espaços em branco;
    - Uma linha contendo o cupom de desconto escolhido (10% ou 20%).

### Saída
- O programa deve exibir uma única linha contendo o valor total de todos os pedidos com o desconto aplicado, no seguinte formato:

    - Valor total: XX.YY, onde "XX.YY" é a soma de todos os pedidos com desconto em formato de duas casas decimais após a vírgula.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
3                  |
Pizza 29.90        |
Hambúrguer 15.50   | Valor total: 47.16
Refrigerante 7.00  | 
10%                |
-----              | ---------------------------------
2                  |
Salada 12.00       | 
Suco 10.50         | Valor total: 18.00
20%                | 
-----              | ---------------------------------
4                  | 
X-Burger 19.99     |
Salada 29.99       |
Sushi 61.00        | Valor total: 96.78
Pudim 10.00        |
20%                |

### Código:


```python
def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
 
    cupom_desconto = input()
  
    if cupom_desconto == "10%":
        total = total * 0.9
    elif cupom_desconto == "20%":
        total = total * 0.8
    
    print(f"Valor total: {total:.2f}")
 
 
if __name__ == "__main__":
    main()
```

    3
    Pizza 29.90
    Hambúrguer 15.50
    Refrigerante 7.00
    10%
    Valor total: 47.16
    

[voltar](#ancora)

<a id="ancora5"></a>
## Desafio: Identificando Pedidos Veganos

### Desafio
O objetivo deste programa é ajudar a equipe do Restaurante Veggieworld a identificar rapidamente os pedidos veganos e não veganos e informar as calorias de cada prato definido pelo cliente. O programa deve solicitar ao usuário o número de pedidos que serão feitos e, em seguida, pedir informações sobre cada pedido, incluindo se o prato é vegano ou não (usando as opções "s" para sim e "n" para não) e a quantidade de calorias. Ao final, o programa deve exibir uma lista de todos os pedidos com suas informações correspondentes.

### Entrada
- Um inteiro n, que representa o número de pedidos que o usuário deseja fazer.
- Para cada pedido, o usuário deve inserir:
   - O nome do prato;
   - A quantidade de calorias do prato;
   - Se o prato é vegano ou não (usando as opções "s" para sim e "n" para não).

### Saída
- O programa deve exibir uma lista de todos os pedidos com suas informações correspondentes, incluindo o nome do prato, se é vegano ou não, e a quantidade de calorias, no seguinte formato:

    - Pedido X: NOME_DO_PRATO (EH_VEGANO?) - YYY calorias, onde "X" é o número do pedido, "NOME_DO_PRATO" é o nome do prato, "EH_VEGADO?" indica se o prato é vegano (escrever "Vegano" ou "Nao-vegano"), e "YYY" é a quantidade de calorias do prato.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.



Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
1                      |
Hamburguer de lentilha |
300                    | Pedido 1: Hamburguer de lentilha (Vegano) - 300 calorias
s                      | 
-----                  | ---------------------------------
2                      | 
Pizza                  |
450                    | Pedido 1: Pizza (Nao-vegano) - 450 calorias
n                      |
Sushi                  | Pedido 2: Sushi (Nao-vegano) - 200 calorias
200                    |
n                      |


### Código:


```python
numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False
    
    opcao_vegano = input()
    if opcao_vegano == "s":
        ehVegano = True

    if ehVegano:
        tipo_vegano = "Vegano"
    else:
        tipo_vegano = "Nao-vegano"

    print(f"Pedido {i}: {prato} ({tipo_vegano}) - {calorias} calorias")

```

    2
    Pizza
    450
    n
    Pedido 1: Pizza (Nao-vegano) - 450 calorias
    Sushi
    200
    n
    Pedido 2: Sushi (Nao-vegano) - 200 calorias
    

[voltar](#ancora)


```python

```
