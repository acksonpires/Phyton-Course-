# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Novo salário: R$'))
n = s + (s*0.15)
print('Seu salário de R${} com 15% de aumento fica R${:.2f}'.format(s, n))
