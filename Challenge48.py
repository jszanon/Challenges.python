''' Challenge 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3
e que se encontram no intervalo de 1 até 500 '''

soma = 0 #conceito de acumulador
cont = 0 #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c #conceito de acumulador, aqui eu estou acumulando números
        cont += 1 #o contador conta mais 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
