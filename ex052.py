#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        cont = cont + 1
if cont == 2:
    print('Ele é primo')
else:
    print('Ele NÃO é primo')
