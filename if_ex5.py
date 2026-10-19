quant_maça = int(input("Digite a quantidade de maçãs compradas: "))
if quant_maça < 12:
    print(f"O valor a ser pago é R${quant_maça * 1.30}")
else:
    print(f"O valor a ser pago é R${quant_maça * 1.00}")
    