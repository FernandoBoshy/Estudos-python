import random
pog = int(input('tente adivinhar meu numero: '))
pog_random = random.randint(0,5)
if pog == pog_random:
    print('voce acertou, meu numero era {} mesmo'.format(pog))
else:
    print('voce errou, meu numero era {}'.format(pog_random))