from math import sqrt, ceil, floor
pog = int(input('a raiz desse numero: '))
raiz = sqrt(pog)
print('a raiz do numero {:.5f} é igual a {:.5f}'.format(pog, raiz))


medida = int(input('valor em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('mm = ', mm)
print('cm = ', cm)
print('dm = ', dm)
print('m = ', medida)
print('dam = ', dam)
print('hm = ', hm)
print('km = ', km)

for K in "Pogge rs":
    print(K)