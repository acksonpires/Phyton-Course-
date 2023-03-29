def contador(inicio, fim, passo):
    if passo == 0 or passo == -1:
        passo = 1
    if inicio <= fim:
        while True:
            print(f'{inicio} ', end=' ')
            inicio += passo
            if inicio == fim or inicio > fim:
                if inicio == fim:
                    print(f'{inicio} ', end=' ')
                print('FIM!')
                break
    elif inicio >= fim:
        while True:
            print(f'{inicio} ', end=' ')
            inicio -= passo
            if inicio == fim or inicio < fim:
                if inicio == fim:
                    print(f'{inicio} ', end=' ')
                print('FIM!')
                break
    print('=-' * 30)


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print(f'Contagem de {i} até {f} de {p} em {p}')
contador(i, f, p)
