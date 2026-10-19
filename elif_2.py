"""2) Entrar com salário de uma pessoa e imprimir o desconto do INSS segundo tabela abaixo:
menor ou igual a 900 - isento 
maior que 900 e menor ou igual a 1200 - 10%
maior que 1200 e menor ou igual a 2000 - 15% 
maior que 2000 - 27,5%"""

salario = float(input("Digite o salário: "))
if salario <= 900:
    print("Isento")

elif salario >900 and salario <= 1200:
    desconto = salario * 0.10
    print(f"Desconto de 10%: R$ {desconto:0.2f}")

elif salario > 1200 and salario <= 2000:
    desconto = salario *0.15
    print(f"Desconto de 15%: R$ {desconto:0.2f}")

else:
    desconto = salario * 0.275
    print(f"Desconto de 27,5%: R$ {desconto:0.2f}")
    
        
