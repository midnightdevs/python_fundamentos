class Livros:
    def __init__(self, titulo, autor, genero_literario, ano):
        self.titulo  = titulo
        self.autor = autor
        self.genero = genero_literario
        self.ano = ano
    def imprime_dados(self):
        print(f'titulo {self.titulo}')
        print(f'autor {self.autor}')
        print(f'genero_literario {self.genero}')
        print(f'ano {self.ano}')
        
meu_livro = Livros(titulo= 'A ilha', autor= 'Eduardo', genero_literario= 'suspense', ano= '2022') 
meu_livro.imprime_dados()   