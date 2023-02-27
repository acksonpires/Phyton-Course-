#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = maisdemil = preçobarato = c = 0
nomebarato = ''
while True:
    print('--' * 30)
    print('LOJA SUPER BARATÃO')
    print('--' * 30)
    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('R$'))
    c += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if c == 1 or preço < preçobarato:
        preçobarato = preço
        nomebarato = nome
    fim = ' '
    while fim not in 'SN':
        fim = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if fim == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${preçobarato}')
