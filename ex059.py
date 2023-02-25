#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
valor = 0
while valor != 5:
    valor = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>> Qual é a sua opção?'''))
    if valor == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif valor == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif valor == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif valor == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        print('Opção inválida! Tente novamente!')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('FIM')
