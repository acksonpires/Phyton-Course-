def titulo(txt):
    print(txt)
    print('--' * 30)


def area(a, b):
    resultado = a * b
    print(f'A área de um terreno {a}x{b} é de {resultado}m²')


titulo('CONTAGEM DE TERRENOS')
largura = float(input('LÁRGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)


