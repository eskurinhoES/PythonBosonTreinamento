import random

valor = random.randint(1,100)
print(valor)

print('Gerar dez números aleatórios entre 1 e 1000')
c = 1
for i in range(10):

    n = random.randint(1,1000)
    print(f'O número {c} gerado foi: {n}.')
    c += 1
print('FIM')
