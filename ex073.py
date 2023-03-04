#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Corinthians.

times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia',
         'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
         'Internacional', 'Palmeiras', 'Bragantino', 'São Paulo',
         'Vasco da Gama')
print('-=' * 15)
print(f'Lista de timesdo Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')

