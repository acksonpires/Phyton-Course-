# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
dados = dict()
pessoas = list()
mulheres = list()
total = soma = média = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    if dados['sexo'] in 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    total += 1
    soma += dados['idade']
    média = soma / total
    pessoas.append(dados.copy())
    dados.clear()
    resp = str(input('Quer continuar? [S/N]'))
    while resp not in 'SsNn':
        print('ERRO! Responda apenas S ou N')
        resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'A) Ao todo temos {total} pessoas cadastradas.')
print(f'B) A média de idade é de {média} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v} ; ', end='')
        print()
print('Encerrado')