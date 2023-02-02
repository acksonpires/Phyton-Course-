#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
p3 = int(input('Terceiro valor: '))
if p1 > p2 and p1 > p3:
    maior = p1
if p2 > p1 and p2 > p3:
    maior = p2
if p3 > p1 and p3 > p2:
    maior = p3
print('O maior valor digitado foi {}'.format(maior))
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3
print('O menor valor digitado foi {}'.format(menor))
