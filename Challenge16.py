'''Challenge 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
sua porção inteira '''

from math import trunc
num = float(input('Digite um número real: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}.')