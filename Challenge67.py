''' Challenge 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo '''

print('-------------TABUADA-------------')
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print('Programa tabuada encerrado. Volte sempre!')
        break
    for t in range(1,11):
        print(f'{num} x {t} = {num*t}')
    print('---------------------------------')
