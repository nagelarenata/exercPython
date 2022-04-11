from time import sleep
print('-=-'*20)
print('Radar eletrônico')
print('-=-'*20)
vel=float(input('Qaul é a sua velocidade atual? '))
print('PROCESSANDO...')
sleep(2)
p = (vel-80) * 7
if vel>80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80 Km/h \nVocê deve pagar uma multa de R${p:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
    

