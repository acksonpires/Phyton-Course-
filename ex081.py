#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostrre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
contN = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    contN += 1
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print(f'Você digitou {contN} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem crescente são {lista} ')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado dentro da lista')