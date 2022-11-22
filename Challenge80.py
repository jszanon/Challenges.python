'''Challenge 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort( )).
No final mostre a lista ordenada na tela.'''

num = list()
for cont in range(0, 5):
    numero = int(input(f'Digite um número na posição {cont}: '))
    for chave, valor in enumerate(num):
        if numero < valor:
            num.insert(chave, numero)
            break
    else:
        num.append(numero)
print(f'Os números digitados para a lista, de forma ordenada foram {num}')
