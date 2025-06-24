from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    materias = Column(String, nullable=False)
    alunos = Column(Integer, ForeignKey('aluno.id'))
    comentarios = Column(Integer, ForeignKey('comentario.id'))
    aulas = Column(Integer, ForeignKey('aula.id'))



