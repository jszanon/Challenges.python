'''Challenge 82: Crie um programa que vai ler vários numero e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas valores pares e valores impares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for cont in range(len(num)):
    if num[cont] % 2 == 0:
        par.append(num[cont])
    else:
        impar.append(num[cont])
print(f'Os números digitados foram {num}')
print(f'Os números pares são {par}')
print(f'Os números ímpares são {impar}')
