''' Challenge 63: Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequencia de Fibonacci.
Ex: 0 – 1 – 1 -  2 – 3- 5 - 8 '''

n = int(input('Digite um número inteiro: '))
t1 = 0 #ultimo numero
t2 = 1 #penultimo numero
print(f'{t1} ⇾ {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' ⇾ {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ⇾ FIM')
