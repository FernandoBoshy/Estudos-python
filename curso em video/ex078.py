list = []
for x in range(0,5):
    list.append(int(input(f'{x+1}º valor: ')))
print(f'sua lista: {list})')
list.sort()
print(f'sua lista organizada: {list}')
print(f'o primeiro valor é {list[0]} e o ultimo é {list[-1]}')