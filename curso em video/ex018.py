import math

pog1 = int(input('digite o angulo: '))
seno = math.sin(math.radians(pog1))
coseno = math.cos(math.radians(pog1))
tang = math.tan(math.radians(pog1))

print('o angulo sendo {} \n seu seno é {:.2f} \n seu coseno é {:.2f} \n sua tangente é {:.2f}'.format(pog1, seno, coseno,tang))