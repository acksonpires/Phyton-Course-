# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

print('=+' * 30)
print('       JOGA NA MEGA SENA     ')
print('-=' * 30)
total = int(input('Quantos jogos você quer? '))

print('-=' * 30)
print('< BOA SORTE! >')
