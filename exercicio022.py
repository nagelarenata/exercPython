n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome completo em maiúsculo é {n.upper()}')
print(f'Seu nome completo em minúsculo é {n.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))