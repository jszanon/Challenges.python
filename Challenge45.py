# Challenge 45: Crie um programa que faça o computador jogar Jokenpô com você

#Definindo os itens
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print(''' Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print(f'Computador jogou {(itens)[computador]}!')
print(f'Jogador jogou {itens[jogador]}!')
print('-=' * 12)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada inválida!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inválida!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
