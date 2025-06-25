import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, String, Integer
from database.db_connections.db import session, Base

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    materias = Column(String(500), nullable=False)
    #alunos = Column(Integer, ForeignKey('aluno.id'), nullable=True)
    #comentarios = Column(Integer, ForeignKey('comentario.id'), nullable=True)
    #aulas = Column(Integer, ForeignKey('aula.id'), nullable=True)

class OperacoesCurso(Curso):
    def cadastrar_curso():
        print("---------CADASTRO DE CURSO---------")
        nome = input(str("Digite o nome do curso: "))
        materias = input(str("Digite as materias deste curso: "))
        if not all ([nome, materias]):
            print("Preencha todos os campos!")
            return
        verificar_cadastro = session.query(Curso).filter(Curso.nome == nome, Curso.materias == materias).first()
        if verificar_cadastro:
            print("Curso ja cadastrado")
        else:
            novo_curso = Curso (nome = nome, materias = materias)
            session.add(novo_curso)
            session.commit()
            print("Curso cadastrado com sucesso!")

    def listar_curso():
        print("---------LISTA DE CURSOS---------")
        cursos = session.query(Curso).all()
        if not cursos:
            print("Nenhum curso cadastrado!")
        else:
            for c in cursos:
                print(f"ID: {c.id} Nome: {c.nome} Materias: {c.materias}")

    def alterar_curso():
        print("-----------ALTERAR CURSO-----------")
        id = input("Digite o id do curso que deseja alterar: ")
        verificar = session.query(Curso).filter(Curso.id == id).first()
        if not verificar:
            print("Curso não encontado!")
        else:
            nome = input("Digite o novo nome do curso: ")
            materias = input("Digite as novas materias do curso: ")
            verificar.nome = nome
            verificar.materias = materias
            session.commit()
            print("Curso atualizado!")
    
    def excluir_curso():
        print("-----------EXCLUIR CURSO-----------")
        id = input("Digite o ID do curso que deseja excluir: ")
        verificar = session.query(Curso).filter(Curso.id == id).first()
        if not verificar:
            print("Curso não encontrado!")
        else:
            session.delete(verificar)
            session.commit()
            print("Curso deletado com sucesso!")





