#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro?'))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
