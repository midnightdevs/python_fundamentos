class controle_remoto:
    marca = 'samsung'
    cor = 'preto'

controle = controle_remoto()

print(controle.marca, controle.cor)


class aluno:
    def __init__(self, nome, turma, portugues, ciencias, matematica):
        self.nome = nome
        self.turma = turma
        self.portugues = portugues 
        self.ciencias = ciencias 
        self.matematica = matematica 
        

    def passou_de_ano(self, materia):
        passou = None
        materia = materia.lower()

        if materia == 'matemática':
            passou = self.matematica >= 7
        
        if materia == 'potuguês':
            passou = self.matematica >= 7
        
        if materia == 'ciências':
            passou = self.matematica >= 7

        if passou:
            print(f'O aluno passou em {materia}')

        if not passou and passou is not NONE:
            print(f'O aluno não passou em {materia}')

        if passou is NONE:
            print('O aluno ainda prescisa cursar a matéria informada')

# falta arrumar**
        

pessoa = aluno('João','3 A', 10, 5)
pessoa.passou_de_ano()