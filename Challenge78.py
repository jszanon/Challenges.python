'''Challenge 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posicão {cont}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos in range(0, 5):
    if valores[pos] == max(valores):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos in range(0,5):
    if valores[pos] == min(valores):
        print(f'{pos}...', end='')
