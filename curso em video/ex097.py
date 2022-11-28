def escreva(x):
    linhas = len(x)
    print('~'* linhas)
    print(x)
    print('~'*linhas)

while True:
    mensagem = str(input('Escreva uma mensagem(000 para sair): '))
    if mensagem == '000':
        break
    escreva(mensagem)