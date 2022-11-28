from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('quantos jogos: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
sleep(2)

sorteio = []
cont2 = 0
while True:
    num2 = randint(1,60)
    if num2 not in sorteio:
        sorteio.append(num2)
        cont2 += 1
    if cont2 >= 6:
        break
print('=-.-' * 10,'=')
sorteio.sort()
print(sorteio)

for x, n2 in enumerate(jogos):
    if n2 == sorteio:
        print(f'o jogo {x+1} foi sorteado com os valores {n2}')