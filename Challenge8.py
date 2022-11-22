# Challenge 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite uma distância em metros: '))
cent = metros * 100
mili = metros * 1000
print(f'A medida de {metros}m é {cent:.0f}cm e {mili:.0f}mm.')