class Livro:
    
    def __init__(self,titulo,autor,genero_literario,ano):

        self.titulo = titulo
        self.autor = autor
        self.genero_literario = genero_literario
        self.ano = ano 

    def escrever(self):
        print(f' Titulo: {self.titulo}\n Autor: {self.autor}\n Gênero: {self.genero_literario}\n Ano: {self.ano}')

book = Livro('Harry Potter','Rowling','Fantasia',2001)
book.escrever()

