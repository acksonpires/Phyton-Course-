#  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
cadastro = list()
while True:
    pessoa = [[], [[], []], []]
    pessoa[0] = str(input('Nome: '))
    pessoa[1][0] = float(input('Nota 1: '))
    pessoa[1][1] = float(input('Nota 2: '))
    pessoa[2] = (pessoa[1][0] + pessoa[1][1]) / 2
    cadastro.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('No   Nome    Média')
print('--' * 15)
for i, l in enumerate(cadastro):
    print(f'{i}     {l[0]}     {l[2]}  ')
print('--' * 15)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if aluno == 999:
        break
    print(f'Notas de {cadastro[aluno][0]} são {cadastro[aluno][1]} ')
