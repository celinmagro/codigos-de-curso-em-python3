from math import hypot

print('Catetos e Hipotenusa')
print('='*40)
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catop, catadj)
print(f'\nA hipotenusa vai medir {hip:.2f}')
print('='*40)
