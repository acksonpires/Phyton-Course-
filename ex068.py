#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
computador = randint(0, 10)
c = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('--' * 15)
    total = computador + jogador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if escolha == 'P' and total % 2 == 0:
        print('DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        c += 1
    elif escolha == 'I' and total % 2 == 1:
        print('DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        c += 1
    elif escolha == 'P' and total % 2 == 1:
        print('VOCÊ PERDEU')
        break
    elif escolha == 'I' and total % 2 == 0:
        print('VOCÊ PERDEU')
        break
    else:
        print('Opção inválida. Aperte P para Par e I para Ímpar!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {c} vezes')
