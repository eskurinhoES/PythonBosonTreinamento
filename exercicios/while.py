nome = None

while True:
    print('Digite seu nome ou x(X) para sair:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo(a) {nome}!')
print('Até logo!')
