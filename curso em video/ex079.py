lista = []
valor = 0
condição = True
while condição:
    valor = int(input('digite um valor, ou digite ''0'' para sair: '))
    if valor == 0:
        break
    if valor in lista:
        print('valor ja adicionado, tente outro...')
        lista.remove(valor)
    lista.append(valor)

print(f'a lista de números: {lista}')
lista.sort()
print(f'a lista em ordem crescente: {lista}')