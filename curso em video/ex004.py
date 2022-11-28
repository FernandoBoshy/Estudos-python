pog = input('digite algo: ')
print('o tipo desse valor é: ', type(pog))
print('só tem espaços? ', pog.isspace())
print('está tudo em maiusculo? ', pog.isupper())
print('está tudo em minusculo? ', pog.islower())
print('é um numero? ', pog.isnumeric())
print('é uma palavra? ', pog.isalpha())
print('é alphanumerico? ', pog.isalnum())
print('está capitalizado? ', pog.istitle())
print(' ', pog.isascii(), pog.isdecimal(), pog.isdigit(), pog.isidentifier(), pog.isprintable())

pog2 = ("nice", 'pogger')
pog3 = ['pog', 'nice', 2]
pog4 = {'pog', 'eleven'}
pog6 = {'pog': 3, 'nice' : 'poggers'}
pog5 = True
print((type(pog2),
       type(pog3),
       type(pog4),
       type(pog5),
       type(pog6)))

def xx():
    pass
print(xx)