valor = int(input('digite um valor para mostrar sua tabuada: '))
while valor >= 0:
    for mult in range(1, 11):
        print(f'{valor} X {mult} = {valor*mult}')
    valor = int(input('digite outro valor: '))
    if valor <= -1:
        break
    print(f'Digite um valor negativo para saír')
print(f'Fim do processo')
