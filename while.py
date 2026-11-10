"""resp = "S"
i = 1
cont = 0
while resp == "S":
    idade = int(input(f"Digite o valor {i}: "))
    if idade == 30:
        cont = cont + 1
    resp = str.upper(input("Deseja continuar a digitar as idades? S/N: "))
    i+= 1
print(f"O total de idades iguais a 30 foi de {cont} pessoa(s).")"""



"""resp = "S"
i = 1
cont = 0
while resp == "S":
    numero = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    resp = str.upper(input("Deseja continuar a fazer mais tabuadas? S/N: "))
    i+= 1"""

resp = "S"
i = 1
cont = 0
soma_avista = 0
soma_aprazo = 0
while resp == "S":
    valor_compra = float(input("Digite o valor da compra: "))
    codigo = int(input("Digite o código da transação: 1  - À Vista, 2 - A Prazo"))
    if codigo == 1: 
        soma_avista += valor_compra
    elif codigo == 2:
        soma_aprazo += valor_compra
    resp = str.upper(input("Deseja continuar a fazer mais compras? S/N: "))
i+= 1
print(f"O total das compras à vista foi de R${soma_avista}")
print(f"O total das compras à prazo foi de R${soma_aprazo}")

soma_total = soma_avista + soma_aprazo
print(f"O total das compras efetuadas foi de R${soma_total}")

receber_aprazo = soma_aprazo / 3
print(f"O valor a receber pelas ompras a prazo é de R${receber_aprazo}")
