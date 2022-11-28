extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatroze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input("Escreva um número entre 0 a 20: "))

while numero in range(0, 21):
    print(f'Você escreveu {extenso[numero]}')
    numero = int(input('Digite outro número: '))
print('Número inválido, fim do processo')