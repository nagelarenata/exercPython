#Como str
#num = str(input('Digite um número entre 0 e 9999: '))
#separado = num.split()
#print(f'Unidade: {num[3]} /n Dezena: {num[2]} /n Centena {num[1]} /n Milhar: {num[0]}')
#Matem
num = int(input('Digite um número entre 0 e 9999: '))
un = num//1 % 10
dez = num//10 % 10
ctn = num//100 % 10
mil = num//1000 % 10
print(f'A unidade é {un}, a dezena é {dez}, a centena é {ctn} e a unidade de milhar é {mil}')
