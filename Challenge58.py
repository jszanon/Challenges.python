''' Challenge 58: Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer '''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False #ainda não acertou
palpites = 0 #ainda não deu palpite nenhum
while not acertou: #enquanto ele não acertar... #quando isso se tornar falso ele sai do laço
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1 #vai ler o número e adicionar mais 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print(f'Acertou com {palpites} tentativas.Parabéns!')
