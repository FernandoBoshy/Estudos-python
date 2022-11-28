pessoas = []
dados = []
total = peso_acima = peso_abaixo = 0
pessoa_acima = []
pessoa_abaixo = []

while True:
    dados.append(str(input("Digite um nome: ")))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    confirm = str(input('Quer continuar? S/N: ')).upper()
    if confirm == 'N':
        break

for p in pessoas:
    if p[1] > 100:
        peso_acima += 1
        pessoa_acima.append(p[0])
    elif p[1] < 70:
        peso_abaixo += 1
        pessoa_abaixo.append(p[0])
