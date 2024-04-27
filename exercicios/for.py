palavra = str(input('Digite uma palavra a ser impressa: '))
for letra in palavra:
    print(f'{letra}')
print(f'Fim de interação da palavra: {palavra}.')

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

for number in range(inicio, fim):
    print(f'Number: {number}.')
print(f'Essa é a interação de {inicio} a {fim}.')
