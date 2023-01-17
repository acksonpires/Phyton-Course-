# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma áre de 2m².
la = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
ar = la * al
lt = ar / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(la, al, ar))
print('Para pintar essa parede, você precisa de {}l de tinta'.format(lt))
