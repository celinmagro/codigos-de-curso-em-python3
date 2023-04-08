print('='*40)
din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = din / 3.27
print('Com R${:.2f}, você pode comprar U${:.2f}'.format(din, dol))
print('='*40)
