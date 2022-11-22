'''Challenge 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.'''

listnum = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listnum:
        listnum.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar!')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
listnum.sort()
print(f'Você digitou os valores {listnum}')
