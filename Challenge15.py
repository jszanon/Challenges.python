''' Challenge 15: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60,00 por dia e R$0,15 por km rodado '''

dias = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km percorridos: '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor total a ser pago é R${pago:.2f}.')