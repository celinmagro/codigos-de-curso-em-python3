print('='*50)
dist = float(input('Digite a distância em metros: '))
print('\nA medida de {:.2f}m corresponde a'.format(dist))
km = dist/1000
hm = dist/100
dam = dist/10
dm = dist*10
cm = dist*100
mm = dist*1000
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n'.format(km,hm,dam,dm,cm,mm))
print('='*50)
