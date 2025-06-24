from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prova(Base):
    __tablename__ = 'prova'
    id = Column(Integer, primary_key=True, autoincrement=True)
    curso = Column(ForeignKey('curso.id'))
    material = Column(Integer, ForeignKey('material.id'))
    titulo = Column(String(25), nullable=False)
    descricao = Column(String)
    nota = Column(String)
    questoes = Column(Integer, ForeignKey('questoes.id'))

class Questao(Base):
    __tablename__ = 'questoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String)
    resposta = Column(String)
    resposta_correta = Column(String)
    

