''' Challenge 49: Refaça o desafio 9, mostrando a tabuada de um numero que o usuário escolher,
só que agora utilizando o laço for '''

num = int(input('Digite um número inteiro para ver a sua tabuada: '))
for t in range(1, 11):
    print(f'{num} x {t} = {num*t}')
