from random import randint

computador = randint(0, 2)
sua_escolha = str(input("escolha pedra, papel ou tesoura: ")).upper()
if computador == 0:
    computador = "PEDRA"
if computador == 1:
    computador = "PAPEL"
if computador == 2:
    computador = "TESOURA"

if sua_escolha == "PEDRA" and computador == "PEDRA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("Empate")
elif sua_escolha == "PAPEL" and computador == "PEDRA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[32mVocê venceu")
elif sua_escolha == "TESOURA" and computador == "PEDRA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[31mVocê perdeu")
elif sua_escolha == "PEDRA" and computador == "PAPEL":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[31mVocê perdeu")
elif sua_escolha == "PAPEL" and computador == "PAPEL":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("Empate")
elif sua_escolha == "TESOURA" and computador == "PAPEL":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[32mVocê venceu")
elif sua_escolha == "PEDRA" and computador == "TESOURA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[32mVocê venceu")
elif sua_escolha == "PAPEL" and computador == "TESOURA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("\033[31mVocê perdeu")
elif sua_escolha == "TESOURA" and computador == "TESOURA":
    print("sua escolha: {} X computador: {}".format(sua_escolha, computador))
    print("Empate")
else:
    print("escolha novamente")