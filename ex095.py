# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
while True:
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
    time.append(jogador.copy())
    gol.clear()
    jogador.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')
    if resp in 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-' * 30)
for k, v in enumerate(time):
    print(f' {k:>3}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogado com código {busca}')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
print('VOLTE SEMPRE')