from math import sin, cos, tan, radians

print('SENO, COSSENO E TANGENTE')
print('='*40)
ang = float(input('Digite o ângulo que você deseja: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'\nO ângulo de {ang} tem o seno de {sin:.2f}')
print(f'\nO ângulo de {ang} tem o cosseno de {cos:.2f}')
print(f'\nO ângulo de {ang} tem a tangente de {tan:.2f}')
print('='*40)
