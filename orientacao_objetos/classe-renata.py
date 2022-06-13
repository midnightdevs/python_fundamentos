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

print(30 * '=')

class Pessoa:
    def __init__(self):
        self.nome = 'Jonas'
        self.sobrenome = 'Ferreira'
        self.endereço = 'Bairro itoupavazinha'


    def person(self):
        print(self.nome, self.sobrenome, self.endereço)

class Funcionario(Pessoa):
    def __init__(self, tipo_de_trabalho):
        super().__init__()
        self.tipo_de_trabalho = tipo_de_trabalho

    def test(self):
        print(self.nome, self.sobrenome, self.endereço, self.tipo_de_trabalho)


first = Pessoa()
second = Funcionario(tipo_de_trabalho = 'Professor')

first.person()
second.test()
    