from random import shuffle

print('SORTEANDO UMA ORDEM NA LISTA')
print('='*40)
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\nA ordem de apresentação será: ', end = ' ')
print(lista)
print('='*40)
