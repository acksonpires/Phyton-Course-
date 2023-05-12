#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(txt):
    while True:
        print('-' * len(txt))
        num = input(txt)
        if num.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return num


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
