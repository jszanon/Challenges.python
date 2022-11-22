'''Challenge 55: Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o
menor peso lidos '''

pmaior = 0
pmenor = 0
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}ª pessoa? '))
    if c == 1:
        pmaior = pmenor = peso
    if peso > pmaior:
        pmaior = peso
    if peso < pmenor:
        pmenor = peso
print(f'O peso maior é {pmaior}.')
print(f'O peso menor é {pmenor}.')

