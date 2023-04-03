from datetime import date


def voto(nasc):
    atual = date.today().year
    idade = atual - nasc
    if idade >= 65:
        print(f'Com {idade}, o voto é OPCIONAL')
    elif idade >= 18:
        print(f'Com {idade}, o voto é OBRIGATÓRIO')
    elif idade >= 16:
        print(f'Com {idade}, o voto é OPCIONAL')
    else:
        print(f'Com {idade}, o voto é NEGADO')


ano_de_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_de_nascimento)
