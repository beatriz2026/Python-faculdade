"""6) faça um algortimo que leia o codigo do departamento em que um funcionário trabalha
(1-secretaria, 2-tesouraria, 3-depto pessoal, 4-amoxarifado), seu nome, salario base e o 
tempo de serviço. O algortim deverá então calcular e imprimir o novo salario base do funcionario
conforme as condições abaixo:
secretaria ou tesouraria - < 4 anos, > 4 anos - aumento de 50%, aumento 60%
depto pessoal - independente - aumento de 30%
almox - > 2 anos, >= 2 anos e <= 4 anos, > 4 anos - aumento de 30%, aumento 40%, aumento 50% """

cod_depart = int(input("Digite o código de departamento no qual o funcionário trabalha (1-secretaria, 2-tesouraria, 3-depto pessoal, 4-amoxarifado): "))
nome = str(input("Digite o nome do funcionário: "))
sal_base = float(input("Digite o salário base do funcionário: "))
temp_serv = float(input("Digite o tempo de serviço do funcionário (anos): "))

if cod_depart == 1 or cod_depart == 2 and temp_serv < 4:
    novo_salario = sal_base * 1.5
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")

else:
    novo_salario = sal_base * 1.6
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")

if cod_depart == 3:
    novo_salario = sal_base * 1.3
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")

if cod_depart == 4 and temp_serv < 2:
    novo_salario = sal_base * 1.3
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")

elif cod_depart == 4 and temp_serv >= 2 and temp_serv <= 4:
    novo_salario = sal_base * 1.4
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")

elif cod_depart == 4 and temp_serv > 4:
    novo_salario = sal_base * 1.5
    print(f"Nome do funcionário: {nome} - Salário antigo: R${sal_base:.2f} - Novo salário: R${novo_salario:.2f}")
            


