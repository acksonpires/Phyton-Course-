#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Me dia um numero: '))
resp = numero % 2
if resp == 1:
    print('Impar')
else:
    print('Par')
