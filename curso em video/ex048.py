limite = int(input('valor: '))

soma = 0
cont = 0
for pog in range(1, limite, 2):
    if pog % 3 == 0:
        soma += pog
        cont = cont + 1

print(cont)
print(soma)