class Aluno:
    """classe que instancia um aluno."""

    def __init__(self,nome,turma,ciencias,matematica,portugues):
        self.nome = nome
        self.turma = turma
        self.ciencias = ciencias
        self.matematica = matematica
        self.portugues = portugues

    def avaliacao_resultado(self,materia):     
        passou = None
        materia = materia.lower()
        if materia == 'ciências':
            passou = self.ciencias >= 7

        if materia == 'matemática':
            passou = self.matematica >= 7

        if materia == 'português':
            passou = self.portugues >= 7

        if passou:
            print(f'O aluno passou em {materia}')

        if not passou and passou is not None:          
            print(f'O aluno não passou em {materia}')

        if passou is None:
            print(f'O aluno ainda precisa cursar a materia informada')

aluno = Aluno(nome= 'Gerfesson',  turma= 'noite', matematica= 4, ciencias= 7, portugues= 8)
aluno.avaliacao_resultado(materia='matemática')
aluno.avaliacao_resultado(materia='ciências')
aluno.avaliacao_resultado(materia='portugues')
aluno.avaliacao_resultado(materia='geografia')


















    
        