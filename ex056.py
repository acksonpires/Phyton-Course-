#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
nomevelho = ''
idadevelho = 0
contmulher = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    #Média de idade do grupo
    soma += idade
    media = soma/4
    #O homem mais velho
    if sexo == 'M' and idade > idadevelho:
        nomevelho = nome
        idadevelho = idade
    #Quantas mulheres têm menos de 20 anos
    if sexo == 'F' and idade < 20:
        contmulher += 1
print('A média de idade do grupo foi de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadevelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contmulher))
