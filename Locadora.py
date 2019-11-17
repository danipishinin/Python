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
    popularidade += 1


@property
def nome(self):
    return self._nome


@nome.setter
def nome(self, nome):
    self._nome = nome


class Filme(Programa):
    def __init__(self, nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

