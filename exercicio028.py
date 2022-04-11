'''from random import randint
from time import sleep
d = int(input('Digite um número de 0 a 5: '))
num = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if 'd==num':
    print('Parabéns, você acertou!')
else:
    print('Que pena! Tente novamente.')'''
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
num=randint(0,5)
d = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if 'num==d':
    print('VOCÊ VENCEU! PARABÉNS!')
else:
    print('GANHEI! Eu pensei no número {num} e você no {d}!')

