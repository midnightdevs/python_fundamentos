class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def andar(self):
        print(f'Eu sou o {self.marca} e eu tô andando')
        self.reserva()

    def reserva(self):
        print('Tô na reserva')


ferrari = Carro('Ferrari', 'F-16')
gol = Carro(marca='Volkswagen', modelo='GOL AP')
print(gol.andar())
print(ferrari.andar())