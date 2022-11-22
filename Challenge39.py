''' Challenge 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
idade:
- Se ele ainda vai se alistar no serviço militar;
- Se é a hora de se alistar;
- Se já passou o tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo '''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
