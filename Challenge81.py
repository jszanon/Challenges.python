'''Challenge 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
- Quantos números foram digitados;
- A lista de valores ordenada de forma decrescente;
- Se o valor 5 foi digitado e está ou não na lista.'''

num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem descrescente são {num}.')
if 5 in num:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')
