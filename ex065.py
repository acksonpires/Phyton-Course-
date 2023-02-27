#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = media = maior = menor = valor = c = 0
resp = ''
while resp != 'N':
    valor = int(input('Digite um número: '))
    c += 1
    soma += valor
    media = soma / c
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('Você digitou {} números e a média foi {}'.format(c, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
