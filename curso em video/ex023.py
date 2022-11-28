pog = int(input('digite um numero entre 0 e 9999: '))
unidade = pog // 1 % 10
dezena = pog // 10 % 10
centena = pog // 100 % 10
milhar = pog // 1000 % 10
print('a unidade é {} \n a dezena é {} \n a centena é {} \n o milhar é {}'.format (unidade, dezena, centena, milhar))