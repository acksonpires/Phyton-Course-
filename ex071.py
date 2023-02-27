#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
c50 = c20 = c10 = c1 = 0
print('==' * 20)
print('{:^35}'.format('BANCO CEV'))
print('==' * 20)
valor = int(input('Que valor você quer sacar? R$'))
print('==' * 20)
while True:
    if valor >= 50:
        valor -= 50
        c50 += 1
        if valor == 0:
            break
    elif valor >= 20:
        valor -= 20
        c20 += 1
        if valor == 0:
            break
    elif valor >= 10:
        valor -= 10
        c10 += 1
        if valor == 0:
            break
    elif valor >= 1:
        valor -= 1
        c1 += 1
        if valor == 0:
            break
print(f'Total de {c50:.0f} cédulas de R$50')
print(f'Total de {c20:.0f} cédulas de R$20' if c20 > 0 else '')
print(f'Total de {c10:.0f} cédulas de R$10' if c10 > 0 else '')
print(f'Total de {c1:.0f} cédulas de R$1' if c1 >0 else '')
print('Volte sempre e tenha um bom dia!')
