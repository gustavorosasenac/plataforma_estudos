from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from database.db_connections.db import Base

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    data_comentario = Column(Date)
    aula = Column(ForeignKey('aula.id'), nullable=True)
    curso = Column(ForeignKey('curso.id'), nullable=True)
    aluno = Column(ForeignKey('aula.id'), nullable=True)
    anonimo = Column(Boolean, default=False)


