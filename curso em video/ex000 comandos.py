'''


LISTAS

_____________________________________________________
valores = list()
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))
for c, v in enumerate(valores):
    print(f'na posição {c} achei o valor {v}!')
print('final')
_____________________________________________________
a = [1, 2, 3, 4]
b = a                   cria uma ligação entre as listas
b[2] = 9                vai mudar o valor de ''a'' também
__________________
a = [1, 2, 3, 4]
b = a[:]                não cria uma ligação entre as listas
b[2] = 9                não mudará o valor de ''a''
__________________


list[X] --- indice de algum valor da lista
list.append(X) ---adiciona um valor no final da lista
list.insert(X, Y) --- adiciona na posição X o valor Y
list.sort --- organiza a lista em ordem
list.sort(reverse = True) --- organiza de forma inversa
list.pop(X) --- elimina um valor da lista(sem o X, elimina o ultimo valor)
list.remove(X) --- elimina o valor X da lista

listas dentro de listas

list = [[x, y, z], [a, b, c], [1, 2]]

TUPLAS


DICIONARIOS

X = dict() ou X = {} para criar um dicionario
dicionario = {nome: algum nome, idade: 20, genero: M}
print(dicionario.values())  ---  printa algum nome, 20 e M
print(dicionario.keys()) --- printa nome, idade e genero
print(dicionario.items()) --- printa ambos


Tratamento de erro


try:
    a = int(input(Digite um numero: )
    b = int(input(Digite outro numero: )
    r = a / b
except:                --- caso o valor digitado ser uma str ou a divisão seja por 0
    Tivemos um problema
else:
    print('resposta: {r})
finally:
    volte sempre...    --- vai acontecer mesmo se o teste der certo ou errado


'''