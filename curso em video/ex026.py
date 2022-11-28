pog = str(input('quantas vezes a letra "A" aparece na frase? ')).upper().strip()
print('a letra A aparece {} vezes na frase.'.format(pog.count('A')))
print('a primeira letra A está na posição {} da frase.'.format(pog.find('A')+1))
print('a ultima letra A está na posição {} da frase.'.format(pog.rfind('A')+1))