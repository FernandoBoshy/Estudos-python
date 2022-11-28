'''
numero = int(input('digite um numero: '))

for n in range(1, numero + 1):
    if numero % n == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(n), end='')
'''

numero = int(input('digite um numero: '))

for n in range(1, numero + 1):
    if numero % n == 0:
        print('\033[33m', end='')
        print('{} '.format(n), end='')

