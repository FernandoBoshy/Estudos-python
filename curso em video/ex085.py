lista = [[], []]

for n in range(0, 7):
    num = int(input('algum valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()

print(f'lista de pares: {lista[0]}')
print(f'lista de impares: {lista[1]}')