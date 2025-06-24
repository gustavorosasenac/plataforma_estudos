from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from DB.db import session, Base

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    data_comentario = Column(Date)
    aula = Column(ForeignKey('aula.id'))
    curso = Column(ForeignKey('curso.id'))
    aluno = Column(ForeignKey('aula.id'))
    anonimo = Column(Boolean, default=False)


