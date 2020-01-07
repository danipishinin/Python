import random

a = input('Digite o seu nome')
b = input('Digite o seu nome')
c = input('Digite o seu nome')
lista = [a,b,c]
ganhador = random.choice(lista)
print(f'E o(a) ganhador(a) é: {ganhador}')