class Pessoa:
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco

    def imprime_nome(self):
        print(self.nome, self.sobrenome)
        
    def imprime_endereco(self):
        print(f'O endereço de {self.nome} é: {self.endereco}')

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, endereco, tipo_de_trabalho):
        super().__init__(nome, sobrenome, endereco)
        self.tipo_de_trabalho = tipo_de_trabalho

    def imprime_nome_funcao(self):
        self.imprime_nome()
        print(f'Sua função é: {self.tipo_de_trabalho}')
        

jonas = Funcionario(nome='Jonas', sobrenome='Rambo', 
                    endereco='Itoupavazinha', tipo_de_trabalho='Professor')


jonas.imprime_nome_funcao()
jonas.imprime_endereco()