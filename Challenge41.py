''' Challenge 41: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirim;
- Até 14 anos: Infantil;
- Até 19 anos: Junior;
- Até 20 anos: Sênior;
- Acima: Master '''

year = int(input('Year of birth: '))
age = 2022 - year

if age <= 9:
    print('Is a little athlete!')
elif age <= 14:
    print('Is a child athlete!')
elif age <= 19:
    print('Is a junior athlete!')
elif age <= 20:
    print('Is a senior athlete!')
else:
    print('Is a master athlete!')

