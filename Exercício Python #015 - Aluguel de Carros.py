dia = int(input('Bom dia, insira quantos dias andará com o carro alugado'))
km = int(input('Insira quantos KM irá percorrer com ele'))

aluguel = (dia*60) + (km * 0.15)

print(f'O preço do aluguel ficará em R${aluguel:.2f}')

