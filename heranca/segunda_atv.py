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

    def funcao_pessoa(self):
        print(f'O {self.nome} trabalha como {self.tipo_de_trabalho}')

usuario = Pessoa('Rua Kamesuke Yonamine 172', 'Leonardo', 'Prado Suzin')
usuario.casa()
usuario.nome_completo()

trabalhador = Funcionario(endereco='Rua Xavantes 1',nome='Erick',sobrenome='Vargas',tipo_de_trabalho='Dev')
trabalhador.funcao_pessoa()