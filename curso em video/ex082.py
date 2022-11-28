lista1 = []
lista2 = []
lista3 = []
continuar = '0'
while True:
    lista1.append(int(input('Digite um valor: ')))
    continuar = str(input('Continuar? S/N: ')).lower()
    if continuar == 'n':
        break

for x in lista1:
    if x % 2 == 0:
        lista2.append(x)
    else:
        lista3.append(x)
print(lista1)
print(f'Lista de pares: {lista2}')
print(f'Lista de impares: {lista3}')