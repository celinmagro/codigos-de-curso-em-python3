from random import choice

print('SORTEANDO UM ITEM NA LISTA')
print('='*40)
i1 = str(input('Primeiro aluno: '))
i2 = str(input('Segundo aluno: '))
i3 = str(input('Terceiro aluno: '))
i4 = str(input('Quarto aluno: '))
lista = [i1, i2, i3, i4]
escolhido = choice(lista)
print(f'\nO aluno escolhido foi {escolhido}')
print('='*40)
