números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar!')
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
números.sort()
print(f'Você digitou os valores: {números}')
