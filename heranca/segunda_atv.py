class Pessoa:

    def __init__(self,endereco,nome,sobrenome):
        self.endereco = endereco
        self.nome = nome
        self.sobrenome = sobrenome

    def casa(self):
        print(f'Ele mora na rua {self.endereco}')

    def nome_completo(self):
        print(f'Seu nome: {self.nome} {self.sobrenome}.')

class Funcionario(Pessoa):
    def __init__(self, endereco, nome, sobrenome,tipo_de_trabalho):
        self.tipo_de_trabalho = tipo_de_trabalho
        super().__init__(endereco, nome, sobrenome)

    def funcio(self):
        print(f'O {self.nome} trabalha como {self.tipo_de_trabalho}')

exercicio = Pessoa('Rua Kamesuke Yonamine 172', 'Leonardo', 'Prado Suzin')
exercicio.casa()
exercicio.nome_completo()

funcio1 = Funcionario(endereco='Rua Xavantes 1',nome='Erick',sobrenome='Vargas',tipo_de_trabalho='Dev')
funcio1.funcio()