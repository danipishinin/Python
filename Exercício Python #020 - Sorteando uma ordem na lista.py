import random

a = input('Digite o seu nome')
b = input('Digite o seu nome')
c = input('Digite o seu nome')
lista = [a,b,c]
apresentador = random.shuffle(lista)
print(f'A ordem de apresentação será:')
print(lista)