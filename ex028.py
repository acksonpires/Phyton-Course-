#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n1 = randint(0, 5)
n2 = int(input(('Em que número eu pensei?')))
print('PROCESSANDO...')
sleep(3)
if n1 == n2:
    print('Parabéns você acertou!')
else:
    print('Que pena, vc errou! Eu pensei no número {}'.format(n1))
