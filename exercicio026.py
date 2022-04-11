n1=str(input('Escreva uma frase: ')).strip().upper()
print('A letra A aparece {} vezes.'.format(n1.count('A')))
print('A primeira vez que a letra A aparece é na posição {}'.format(n1.find('A')+1))
print('A última vez que a letra A aparece é na posição {}'.format(n1.rfind('A')+1))