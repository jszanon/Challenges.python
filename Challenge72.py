'''Challenge 72:Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até 20. Seu programa deverá ler um programa pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >=0 and num <=20:
        print(f'Você digitou o número {extenso[num]}.')
        break
    if num > 20:
        print(f'Número inválido.', end='')
