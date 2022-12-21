print('Pintando Parede')
print('='*40)
larg = float(input('Largura da parede em m: '))
alt = float(input('Altura da parede em m: '))
a = larg * alt
l = a / 2
print('\nSua parede tem a dimensão: {:.2f}x{:.2f} \nSua área é de: {:.2f}m²'.format(larg, alt, a))
print('\nPara pintar essa parede você precisará de {:.1f}L de tinta'.format(l))
print('='*40)
