#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(txt):
    while True:
        print('-' * len(txt))
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            break
        else:
            return num


def leiaFloat(txt):
    while True:
        print('-' * len(txt))
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            break
        else:
            return num



n = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'Os valores digitados foram {n} e {f}')
