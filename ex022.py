print('ANALISADOR DE TEXTOS')
print('>-'*20)
nome = str(input('Digite um nome completo: ')).strip()
print(f'''\nO nome com todas as letras maiúsculas: {nome.upper()}
O nome com todas as letras minúsculas: {nome.lower()}
Quantas letras ao todo: {len(nome)-nome.count(' ')}
Quantas letras tem o primeiro nome: {len(nome.split()[0])}''')
print('>-'*20)
