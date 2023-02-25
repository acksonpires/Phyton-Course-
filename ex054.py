#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
velho = 0
novo = 0
for c in range(1, 8):
    nasc = int(input(('Em que ano a {}ª pessoa nasceu? '.format(c))))
    if (atual - nasc < 18):
        novo += 1
    else:
        velho += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(velho))
print('E também tivemos {} pessoas menores de idade'.format(novo))