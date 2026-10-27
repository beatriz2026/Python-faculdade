"""status = 700
match status: 
    case 200:
        print("Sucesso!")
    case 300 | 400:
        print("Erro do cliente.")
    case status if status >= 500 and status <= 700:
        print(f"Erro do servidor: {status}")
    case _:
        print("Status desconhecido.")"""

# Lista de exercícios MATCH CASE:

# 1 - Crie um algoritmo que soliite ao usuário dois números reais e, em seguida, um caractere que representa a operação (+, -, *, /, raiz). Utilize a estrutura case para realizar a operação correspondente e exibir o resultado. Se o operador for inválido, mostre um aviso.

import math
4
"""n1 = float(input("Digite o primeiro número real: "))
n2 = float(input("Digite o o segundo número real: "))
operacao = str(input("Digite o caractere que representa a operação desejada (+, -, *, /, raiz): "))

match operacao:
    case "+":
        soma = n1 + n2
        print(f"A soma de {n1} e {n2} é: {soma}")
    case "-":
        subt = n1 - n2
        print(f"A subtração de {n1} e {n2} é: {subt}")
    case "*":
        mult = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é: {mult}")
    case "/":
        div = n1 / n2
        print(f"A divisão de {n1} por {n2} é: {div}")
    case "raiz":
        raiz = math.sqrt(n1 + n2)
        print(f"A raiz quadrada da soma de {n1} e {n2} é: {raiz}")
    case _:
        print("Operação inválida. Por favor, insira um operador válido.")"""


"""2 - Elabore um programa que exiba o cardápio de uma lanchonete: 
101 - Cachorro-quente (R$ 6,00)
01 - X-Salada (R$ 10,00)
203 - X-Bacon (R$ 12,00)
 204 - X- Mignon Salada ( 35,00)
 205 - X-Frango Sala ( 32,00)
 306 - Refrigerante Coca Cola (R$ 5,00)
 407 - Refrigerante Guaraná (R$ 3,50)
O usuário deve digitar o código do item e a quantidade desejada. O programa
deve calcular o valor total a ser pago usando um match-case para identificar o
preço de cada item """

"""cardapio = "Código\t\tItem\t\tPreço"
separador = "----------------------------------"
linhas = (
    "201\t\tCachorro-Quente\t6.00\n"
    "202\t\tX-Salada\t10.00\n"
    "203\t\tX-Bacon\t12.00\n"
    "204\t\tX-Mignon Salada\t35.00\n"
    "205\t\tX-Frango Salada\t32.00\n"
    "206\t\tCoca Cola\t5.00\n"
    "207\t\tGuaraná\t3.50\n"
)
tabela = f"{cardapio}\n{separador}\n{linhas}"
print(tabela)

codigo = int(input("Digite o código do item desejado: "))
qtde = int(input("Digite a quantidade desejada: "))

match codigo:
    case 201:
        preco = 6.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}") 
    case 202:
        preco = 10.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")
    case 203:
        preco = 12.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")
    case 204:
        preco = 35.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")
    case 205:
        preco = 32.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")
    case 206:
        preco = 5.00
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")
    case 207:
        preco = 3.50
        total = preco * qtde
        print(f"Total a pagar: R$ {total:.2f}")"""


# 3 -  Utilizando o comando match..case, faça um programa que lê como entrada o
#preço de um produto e o código relativo à forma de pagamento de acordo
#com a tabela abaixo, deve ser aplicado o desconto especificado e o programa
#deve exibir os números de prestações e o valor de cada prestação a ser pago.




