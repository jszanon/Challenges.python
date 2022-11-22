''' Challenge 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo (sem considerar os espaços);
- Quantas letras tem o primeiro nome '''

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {(nome.upper())}')
print(f'Seu nome em minúsculas é {(nome.lower())}')
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
