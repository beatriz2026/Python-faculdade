"""3) faça um programa que receba 3 notas de um estudante, calcule e imprima a média final 
e o conceito desse estudante: 
8.1 a 10 - conceito A
7.1 A 8.0 - conceito B
6.1 A 7.0 - conceito C
5.1 A 6.0 - conceito D
menor que 5.0 - conceito E
"""

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 8.1 and media <= 10:
    print(f"Média final: {media:.2f} - Conceito A")

elif media >= 7.1 and media <= 8.0:
    print(f"Média final: {media:.2f} - Conceito B")

elif media >= 6.1 and media <= 7.0:
    print(f"Média final: {media:.2f} - Conceito C")

elif media >= 5.1 and media <= 6.0:
    print(f"Média final: {media:.2f} - Conceito D")

else:
    print(f"Média final: {media:.2f} - Conceito E")