# Método Publico & Método privado.

class Trabalho:
    def __init__(self):
        self.nome = 'midnightdevs'
        self.horario_de_saida = '00:00'

    def hora_saida(self):
        """
        método privado
        """
        print(self.horario_de_saida)

    def informa_nome(nome):
        """
        metodo público
        """
        print(nome)

Trabalho.informa_nome(nome='Eduardo')
instancia = Trabalho()
instancia.hora_saida()

