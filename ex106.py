def ajuda(com):
    help(com)


def título(msg, cor=0):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)


#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!')