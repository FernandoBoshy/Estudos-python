pog = int(input('velocidade do carro: '))
if pog >= 80:
    print('voce foi multado')
    print('terá que pagar {}R$ de multa'.format((pog-80)*7))