#from Locadora import Filme, Serie
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._popularidade = 0

    @property
    def likes(self):
        return self._popularidade

    def n_likes(self):
        self._popularidade += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

tvd = Serie('The Vampire Diaries',2008,8)
tvd.n_likes()
dory = Filme('Procurando Dory',1016,160)
dory.n_likes()

filmes_e_series = [tvd, dory]
playlist_fim_de_semana = Playlist('fim de semana',filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)
