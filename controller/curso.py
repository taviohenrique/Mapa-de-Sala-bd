from model.curso import Curso
from model.area import Area
from view.cadastrarCurso import CadastrarCurso

class CursoController(CadastrarCurso):
    def __init__(self):
        super().__init__()
        self.btnCadastrarCurso.clicked.connect(self.cadastroDeCurso)
        self.addArea()
        self.show()
        
    def cadastroDeCurso(self):
        areaRetorno, nomeRetorno, ofertaRetorno, periodoRetorno, cargaRetorno, horasRetorno, alunosRetorno = self.getCadastroCurso()
        cursoModel = Curso(areaRetorno, nomeRetorno, ofertaRetorno, periodoRetorno, cargaRetorno, horasRetorno, alunosRetorno)
        cursoModel.cadastrar_curso()
        
    def addArea(self):
        areaClass = Area('Teste')
        resultado = areaClass.consulta_nome_area()
        for i in resultado:
            lista = []
            lista.append(i)
        print(lista)       