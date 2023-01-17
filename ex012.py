# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto? '))
d = p - (p*0.05)
print('O produto que custa R${}, com 5% de desconto, fica R${:.2f}'.format(p, d))
