# Esceva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kmp = float(input('Quantos Km percorridos: '))
x = int(input('Por quantos dias ele foi alugado: '))
precoKm = kmp * 0.15
precoD = x * 60
print('Você tem que pagar R${:.2f} pelos dias utilizados e R${:.2f} pelos Km rodados, no total de R${}'.format(precoKm, precoD, precoKm+precoD))


