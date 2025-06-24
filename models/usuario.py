from sqlalchemy import Column, String, Integer, Date, ForeignKey
from DB.db import session, Base

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    genero = Column(String)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    cidade = Column(String)
    estado = Column(String)
    pais = Column(String)
    cep = Column(String)

class Professor(Usuario):
    __tablename__ = 'professor'
    materias = Column(String)
    curso = Column(Integer, ForeignKey('curso.id'))
    aulas = Column(Integer, ForeignKey('aula.id'))

class Aluno(Usuario):
    __tablename__ = 'aluno'
    cursos = Column(Integer, ForeignKey('curso.id'))
    em_progresso = Column(Integer, ForeignKey('aula.id'))
    aulas = Column(Integer, ForeignKey('aula.id'))
    materias = Column(String)
    provas = Column(Integer, ForeignKey('prova.id'))

