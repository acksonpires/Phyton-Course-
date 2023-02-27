#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = 0
while True:
    print('---' * 20)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('---' * 20)
    if num < 0:
        break
    for c in range(0, 11):
        produto = num * c
        print(f'{num:2} x {c:2} = {produto:2}')
 
