#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = c = s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    if n != 999:
        s += n
        c += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))