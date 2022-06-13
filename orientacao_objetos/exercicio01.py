"""crie uma classe livros que tenha como argumento:

titulo
autor
genero literario
ano
crie um método que imprima de forma ordenada, os atributos da classe livro."""

class Livros:
    def __init__(self,titulo,autor,genero,ano):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
    def imprime_dados(self):
        print(self.titulo)    
        print(self.autor)
        print(self.genero)
        print(self.ano)

meu_livro = Livros(titulo= 'A noite', autor='Gerfesson',genero='desconhecido',ano='2045')   
meu_livro.imprime_dados()




















class Funcionário(Pessoa):
    def __init__(self,tipo_de_trabalho):


