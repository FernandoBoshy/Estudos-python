from random import randint

jogadores = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}

for x, y in jogadores.items():
    print(f'o {x} tirou o numero {y} nos dados')

