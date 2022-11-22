''' Challenge 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
(frase lida de trás pra frente e tem o mesmo sentido de frente pra trás), desconsiderando os espaços.
Exemplo:
Apos a sopa (leia de trás para frente)
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona '''

frase = str(input('Digite uma frase: ')).strip().upper() #li a frase e tirei os espaços (antes de depois) e coloquei em letra maiúscula
palavras = frase.split() #splitei a frase para que ele gere uma lista
junto = ''.join(palavras) #juntei a tudo em uma única string
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto: #testei se o inverso é a mesma coisa que o junto
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
