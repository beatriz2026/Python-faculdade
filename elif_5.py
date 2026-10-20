"""5) Elaborar um algoritmo que leia o valor de dois números inteiros e a operação 
aritmética desejada; calcule, então a resposta adequada. Utilize os símbolos da tabela
a seguir para ler qual a operação aritmética escolhida.
simbolo + é adição
- é subtração
* é multiplicação
/ é divisão"""

nu_1 = float(input("Digite o primeiro número: "))
nu_2 = float(input("Digite o segundo número: "))
operacao = str(input("Digite a operação desejada (+, -, *, /): "))

if operacao == "+":
    resultado = nu_1 + nu_2
    print(f"O resultado da adição é: {resultado:.2f}")

elif operacao == "-":
    resultado = nu_1 - nu_2
    print(f"O resultado da subtração é: {resultado:.2f}")

elif operacao == "*":
    resultado = nu_1 * nu_2
    print(f"O resultado da multiplicação é: {resultado:.2f}")

elif operacao == "/" and nu_2 != 0:
    resultado = nu_1 / nu_2
    print(f"O resultado da divisão é: {resultado:.2f}")

else:
    print("Operação inválida ou divisão por zero não permitida.")
            
