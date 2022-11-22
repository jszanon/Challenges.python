''' Challenge 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores '''

r = 'S'
soma = quantidade = media = maior = menor = 0
while r == 'S':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
