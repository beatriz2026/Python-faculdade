"""1) ler dois valores e imprimir uma das tres mensagens a seguir:
- "Números iguais" caso os números sejam iguais
- "Primeiro é maior" caso o primeiro seja maior que o segundo
- "Segundo é maior" caso o segundo seja maior que o primeiro"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 == n2:
    print("Números iguais")
elif n1 > n2:
    print("Primeiro é maior")
else: 
    print("Segundo é maior")
