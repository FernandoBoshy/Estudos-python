def area(largura,comprimento):
    total = largura * comprimento
    print(f'A área do terreno {largura}x{comprimento} é de {total}m²')


a = float(input('Largura(m): '))
b = float(input('Comprimento(m): '))
area(a, b)