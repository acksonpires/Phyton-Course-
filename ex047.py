# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for c in range(1, 51): #gasta mais processamento da máquina
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou')
for c in range(2, 51, 2):
    print('.', end='')
    print(c, end=' ')
