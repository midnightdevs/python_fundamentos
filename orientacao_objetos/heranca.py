class Gato:
    """Classe Gato pai."""

    def __init__(self, nome, idade):
        self.nome = 'Garfield' if not nome else nome
        self.idade = idade

    def miar(self):
        print(f'Miau Miau')

class Angora(Gato):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def arranha_sofa(self):
        print(f'O gato {self.nome} gosta de arranhar e destruir seu sofá.')

class Persa(Gato):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def hiberna(self):
        print(f'O gato {self.nome} hibernando no sofá.')


gato_angora = Angora(nome='Felix', idade=3)
gato_angora.miar()
gato_angora.arranha_sofa()
print(gato_angora.nome)


gato_persa = Persa(nome='Garfield', idade=5)
gato_persa.miar()
gato_persa.hiberna()

print(gato_angora.nome)