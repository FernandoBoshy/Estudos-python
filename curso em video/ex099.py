from random import randint

def maior(* num):
    print(num)


lista = []
ind = 0
for lis in range(0, randint(3, 10)):
    lis = randint(1, 50)
    print(lis)
    lista.append(lis)
    ind += 1

print(lista)
lista.sort()
quant = len(lista)
print(f'sua lista de numeros contém {quant} valores')
print(f'Os valores são: {lista}, e o maior valor é {lista[-1]}')