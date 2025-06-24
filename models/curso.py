import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from banco.db import session


Base = declarative_base()

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    materias = Column(String, nullable=False)
    #alunos = Column(Integer, ForeignKey('aluno.id'))
    #comentarios = Column(Integer, ForeignKey('comentario.id'))
    #aulas = Column(Integer, ForeignKey('aula.id'))


    def cadastrar_curso():
        print("---------CADASTRO DE CURSO---------")
        c_nome = input(str("Digite o nome do curso: "))
        c_materias = input(str("Digite as materias deste curso: "))
        novo_curso = Curso (nome = c_nome, materias = c_materias)
        session.add(novo_curso)
        session.commit
        print("Curso cadastrado com sucesso!")

    def listar_curso():
        print("---------LISTA DE CURSOS---------")
        cursos = session.query(Curso).all()
        if not cursos:
            print("Nenhum curso cadastrado!")
        else:
            for c in cursos:
                print(f"ID: {c.id} Nome: {c.nome} Materias: {c.materias}")



