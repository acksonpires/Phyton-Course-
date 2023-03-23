# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gol = list()
soma = i = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(1, partidas + 1):
    gol.append(int(input(f'QUantos gols na partida {c}?')))
    soma += gol[i]
    i += 1
jogador['gols'] = gol[:]
jogador['total'] = soma
print('=-' * 30)
print(f'{jogador.items()}')
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
i = 0
for c in range(1, partidas + 1):
    print(f'    => Na partida {c}, fez {gol[i]} gols')
    i += 1

