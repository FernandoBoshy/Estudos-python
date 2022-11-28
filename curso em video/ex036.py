valor_casa = float(input("qual o valor da casa: "))
salario = float(input("Seu salário: "))
parcelas = int(input("quantidade de parcelas em meses: "))

valor_parcela = valor_casa / parcelas
aprovação = salario * (30 / 100)
print("-==" *30)
if valor_parcela > aprovação:
    print("o valor da parcela será de \033[1;31mR${:.2f}\033[0m, então você não pode financiar esta casa".format(valor_parcela))
else:
    print("o valor da parcela será de \033[1;32m{:.2f}\033[0m durante {} meses".format(valor_parcela, parcelas))
print("-==" *30)
