# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.09
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))

