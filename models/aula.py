from sqlalchemy import Column, String, Integer, ForeignKey
from database.db_connections.db import Base

class Aulas(Base):
    __tablename__ = 'aula'
    id = Column(Integer, primary_key=True, autoincrement=True)
    professor = Column(Integer, ForeignKey('professor.id'))
    titulo = Column(String)
    materia = Column(ForeignKey('materia.id'))
    check_in = Column(String)
    comentarios = Column(ForeignKey('comentario.id'))
    material = Column(String)
    provas = Column(Integer, ForeignKey('prova.id'))

