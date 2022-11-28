from random import randint

pog = (randint(0, 100), randint(0, 100), randint(0, 100),
       randint(0, 100), randint(0, 100), )

print(f'a lista de numeros são {pog}')
print(f'Em ordem crescente: {sorted(pog)}')
print(f'O maior valor é {max(pog)}')
print(f'O menor valor é {min(pog)}')