import pygame
from random import randint

computador = randint(0,10)
print('Tente adivinhar meu numero...')
player = int(input('Digite um numero de 0 a 10: '))
contador = 0
print(computador)
while computador != player:
    contador = contador +1
    player = int(input('Tente novamente: '))
print("Parabéns, você acertou com {} tentativas". format(contador))