nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo (F/M): "))
est_civil = str(input("Digite seu estado civil (S/C): "))
ano_casam = int(input("Digite o ano de casamento (se for casado): "))
ano_atual = int(input("Digite o ano atual: "))

tempo_casados = ano_atual - ano_casam
if sexo == "F" or "f" and est_civil == "C" or "c":
        print(f"{nome} está casado (a) há {tempo_casados} anos.")
