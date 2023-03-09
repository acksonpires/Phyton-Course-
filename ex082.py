#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
listaI = list()
listaP = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaP}')
print(f'A lista de ímpares é {listaI}')
