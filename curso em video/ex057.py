sexo = str(input('Digite um sexo M ou F: ')).upper()
while sexo not in 'MF':
    sexo = str(input("Digite um sexo M ou F válido: ")).upper()
print('Bem vindo')