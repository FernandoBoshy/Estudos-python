from time import sleep
def contador(i, f, p):
    if p < 0:
        p = p * -1
    print(f' \ncontagem de {i} até {f} de {p} em {p}')
    cont = i

    if i < f:
        if p == 0:
            p = 1
            while i <= f:
                cont += p
                print(i, end=' ')
                i += p
                sleep(0.3)
        else:
            while i <= f:
                cont += p
                print(i, end=' ')
                i += p
                sleep(0.3)

    elif i > f:
        while i >= f:
            cont -= p
            print(i, end=' ')
            i -= p
            sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez')
i = int(input('Digite o inicio: '))
f = int(input('Digite o final: '))
p = int(input('Digite o passo: '))

contador(i, f, p)