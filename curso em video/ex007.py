pog1 = int(input('um valor: '))
pog2 = int(input('outro valor: '))
pogsoma = pog1 + pog2
pogsub = pog1 - pog2
pogmult = pog1 * pog2
pogdiv = pog1 / pog2
pogdivin = pog1 // pog2
pogpot = pog1 ** pog2
pogmod = pog1 % pog2

print('a soma é {}, a subtração é {}, \n o produto é {}, a divisão é {:.4f},'.format(pogsoma, pogsub, pogmult, pogdiv), end=' ')
print('a divisão inteira é {}, a potencia é {}, \n o modulo é {}'.format(pogdivin, pogpot, pogmod))

pog3 = int(input('mais valores: '))
print('o numero é {}, depois dele é o {} e antes vem o {}'.format(pog3, pog3+1, pog3-1))
print('o numero é {}, seu dobro é {}, seu triplo é {}, e sua raiz é {}'.format(pog3, pog3*2, pog3*3, pog3**0.5))

pog4 = int(input('sua nota: '))
pog5 = int(input('sua outra nota: '))
print('suas notas são {} e {}, então sua média é {}'.format(pog4, pog5, (pog4 + pog5)/2))
