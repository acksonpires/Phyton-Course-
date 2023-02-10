#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
computador = randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida! Tente novamente')
