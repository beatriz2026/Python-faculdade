"""media = 0
total = 0
for i in range(1,6):
    preco = float(input(f"Digite o preço do {i}° produto: "))
    total += preco

media = total / 5
print(f"O total da compra foi de R$ {total}")
print(f"A média dos preços foi de R$ {media}")"""

# 2 - ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20],
# incluindo os valores 10 e 20 no intervalo, e quantos estão fora do intervalo.






# 3) Faça um algoritmo que gere e imprima a tabuada de um número digitado pelo teclado. 
"""numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")"""

# 4) desenvolver um algoritmo que leia o nome e a altura de 15 pessoas. Este programa deverá calcular e mostrar: 
# a pessoa de menor altura do grupo e seu nome e a pessoa de maior altura e seu nome.
"""menor = 9999
maior = 0
for i in range(1,6):
    nome = str(input(f"Digite o nome da {i}° pessoa: "))
    altura = float(input(f"Digite a altura da {i}° pessoa: "))
    if altura < menor:
        menor = altura
        pessoa_menor = nome
    if altura > maior:
        maior = altura
        pessoa_maior = nome

print(f"A pessoa de menor altura é {pessoa_menor} com {menor}m")
print(f"A pessoa de maior altura é {pessoa_maior} com {maior}m")"""  


"""maior = 0
menor = 9999
for i in range(1,6):
   nome = str(input(f"Digite o nome da {i}ª pessoa: "))
   peso = float(input(f"Digite o peso da {i}ª pessoa: "))
   if peso > maior:
       maior = peso
       nome_damaior = nome
       peso_maior = peso
   elif peso < menor:
       menor = peso 
       nome_domenor = nome
       peso_menor = peso

print(f"A pessoa de maior peso é {nome_damaior} com {peso_maior}kg")
print(f"A pessoa de menor peso é {nome_domenor} com {peso_menor}kg")"""       

# 5) faça um algortimo que receba seis notas de 10 alunos e imprima a média entre essas 6 notas 

for i in range(1,11):
    for x in range(1,7):
        nota = float(input(f"Digite a nota {x} do {i}° aluno: "))
        soma += nota 
        media = soma / 6
        if media <= 5:
            total_reprov += 1
            print(f"Aluno reprovado.")

        elif media > 5 and media <= 7:
            print(f"Aluno de Exame.")

        elif media > 7 and media <= 10:
            total_aprov += 1
            print(f"Aluno Aprovado.") 

        media    

print(f"O total de alunos aprovados é {total_aprov}")
print(f"O total de alunos reprovados é {total_reprov}")




