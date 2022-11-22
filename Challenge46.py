''' Challenge 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artificio, indo de 10 a 0, com uma pausa de 1 segundo entre eles '''

from time import sleep
import emoji
print('Contagem regressiva para os fogos!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('HAPPY NEW YEAR!!! :confetti_ball: :confetti_ball: :confetti_ball:', language = 'alias'))
