#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = str(input('Qual a opção de pagamento? ')).strip()
if opcao == '1':
    desconto = preco - (preco * 0.10)
    print('Sua compra de R${} vai custar R${} no final'.format(preco, desconto))
elif opcao == '2':
    desconto = preco - (preco * 0.05)
    print('Sua compra de R${} vai custar R${} no final'.format(preco, desconto))
elif opcao == '3':
    print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(preco / 2))
elif opcao == '4':
    parcela = int(input('Quantas parcelas? '))
    juros = preco + (preco * 0.20)
    prestacao = juros / parcela
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parcela, prestacao))
    print('Sua compra de R${:.2f} vai curstar R${:.2f} no final'.format(preco, juros))
else:
    print('Opção inválida!')
