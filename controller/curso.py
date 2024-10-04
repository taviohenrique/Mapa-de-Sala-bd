from model.curso import Curso
from view.cadastrarCurso import CadastrarCurso

class CursoController(CadastrarCurso):
    def __init__(self):
        super().__init__()
        # print( dir(self.periodoCurso))
        self.btnCadastrarCurso.clicked.connect(self.cadastroDeCurso)
        self.NOMEDOCOMBOBOX.addItems()
        self.show()
        
    def cadastroDeCurso(self):
        nomeCurso = self.getCadastroCurso()
        cursoModel = Curso(nomeCurso)
        cursoModel.cadastrar_curso()
        
        