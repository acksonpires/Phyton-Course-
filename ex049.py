#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuáda: '))
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, c, n*c))
