import os   
os.system("cls")

op = str.upper(input("tipo combustivel A-Alcool G-Gasolina = "))
qtdeComb = float(input(" digite a quantidade de combustivel = "))

if op == "A":
    if qtdeComb <= 20:
        valorPagar = qtdeComb * 3.34 * 0.97
    else:
        valorPagar = qtdeComb * 3.34 * 0.95
else:
    if qtdeComb <= 20:
        valorPagar = qtdeComb * 4.30 * 0.96
    else:
        valorPagar = qtdeComb * 4.30 * 0.94

if op== "A":
    print(f"Total de Litros {qtdeComb} de Alcool a pagar R$ {valorPagar:0.2f}")
else:
    print(f"Total de Litros {qtdeComb} de Gasolina a pagar R$ {valorPagar:0.2f}")
    