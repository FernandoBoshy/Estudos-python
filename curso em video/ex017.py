from math import hypot, trunc

pog1 = int(input('coloque o cateto adj.: '))
pog2 = int(input('coloque o cateto opos.: '))
pog3 = hypot(pog1, pog2)

print('cateto adj {} e opost {}, hipotenusa {}'.format(pog1, pog2, trunc(pog3)))