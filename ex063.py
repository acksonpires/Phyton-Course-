#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
print('-' * 30)
total = int(input('Quanto termos você quer mostrar? '))
print('-' * 30)
c = 0
p3 = p2 = p1 = 1
print('0 -> 1 -> ', end='')
while c < (total -2):
    print('{}'.format(p3), end='')
    print(' -> ' if c < (total - 3) else ' FIM ', end='')
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    c += 1
