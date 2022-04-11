import math
a = float(input('Digite um ângulo? '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print(f' O seno de {a}º é {s:.2f} \n O cosseno de {a} e {c:.2f} \n A tangente de {a} é {tg:.2f}')
