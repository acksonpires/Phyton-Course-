#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinto', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
end = 'S'
while end == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.')
    print(f'Você digitou o número {cont[num]}')
    end = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

