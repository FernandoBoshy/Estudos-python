'''
Digite um valor
o programa dirá a soma de todos os valores digitados
e a quantidade de valores
'''

soma = 0
cont = 0
while True:
    valor = int(input("Digite um valor: "))
    if valor == '':
        valor = 0
    if valor == 999:
        break
    soma += valor
    cont += 1

print(f'Foram digitados {cont} valores e a soma deles é \033[2;31;32m{soma}\033[m')