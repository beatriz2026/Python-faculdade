nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
media_aprov = 5.0
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 5.0:
    print(f"Aprovado! Sua média foi {media}")
    