import random
pog = random.randint(0, 100)
par = pog % 2
print('o numero é {}'.format(pog))
if par == 0:
    print('par')
else:
    print('impar')