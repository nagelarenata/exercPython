import math
ca=(float(input('Qual é o comprimento do cateto adjacente? ')))
co=(float(input('Qual é o comprimento do cateto oposto? ')))
h = math.hypot(co,ca)
print(f'O comprimento da hipotenusa é {h}')

