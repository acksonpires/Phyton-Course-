# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
valor = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        valor[0].append(num)
    else:
        valor[1].append(num)
print('-=' * 30)
valor[0].sort()
valor[1].sort()
print(f'Os valores pares digitados foram: {valor[0]}')
print(f'Os valores ímpares digitados foram: {valor[1]}')
