valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior: int
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')

