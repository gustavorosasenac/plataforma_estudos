from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    materia = Column(String)
    formato = Column(String(5))
    caminho_arquivo = Column(String)
    aula = Column(Integer, ForeignKey('aula.id'))


