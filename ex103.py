#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome_do_jogador="<desconhecido>", gols_marcados=0):
    print(f'O jogador {nome_do_jogador} fez {gols_marcados} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols_marcados=gols)
else:
    ficha(nome, gols)
