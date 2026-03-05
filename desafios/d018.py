from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.1f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.1f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.1f}')