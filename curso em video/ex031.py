pog = float(input('KM da viagem: '))
print('a viagem terá {:.2f}KM'.format(pog))
if pog <= 200:
    print('sua viagem custará R${:.2f}'.format(pog*0.50))
else:
    print('sua viagem custará R${:.2f}'.format(pog*0.45))