class Livro:
    def __init__(self, titulo, autor, genero_literario, ano):
        self.titulo = titulo
        self.autor =  autor
        self.genero_literario = genero_literario
        self.ano = ano

    def read(self):
        print(self.titulo, self.autor, self.genero_literario, self.ano)

book = Livro(titulo = 'dom queixote', autor = 'Miguel de Cervantes', genero_literario = 'ficção', ano = 1906)
book.read()


class Pessoa:
    def __init__(self, nome, sobrenome, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco


    def imprime_nome(self):
        print(self.nome, self.sobrenome)

    def imprime_endereco(self):
        print(f'O endereço  de {self.nome} é : {self.endereco}')

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, endereco, tipo_de_trabalho):
        super().__init__(nome, sobrenome, endereco)
        self.tipo_de_trabalho = tipo_de_trabalho

    def imprime_nome_funcao(self):
        self.imprime_nome()
        print(f'Sua função é {self.tipo_de_trabalho}')

Jonas = Funcionario(nome = 'Jonas', sobrenome = 'Ferreira', endereco = 'Bairro Itoupavazinha', tipo_de_trabalho = 'Professor')

Jonas.imprime_nome()
Jonas.imprime_endereco()
Jonas.imprime_nome_funcao()    