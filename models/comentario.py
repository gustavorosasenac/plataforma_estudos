import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean
from database.db_connections.db import Base, session
from models.usuario import Usuario


class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100))
    descricao = Column(String(100))
    data_comentario = Column(Date)
    aula = Column(Integer, ForeignKey('aula.id'), nullable=True)
    curso = Column(Integer, ForeignKey('curso.id'), nullable=True)
    aluno = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    anonimo = Column(Boolean, default=False)

class OperacoesComentario(Comentario):
    def cadastrar_comentario():
        print('--------------CADASTRAR COMENTARIO--------------')
        titulo = input('Digite o titulo do comentario: ')
        descricao = input('Digite a descricao do comentario: ')
        data_comentario = input('Digite a data do comentario (YYYY-MM-DD): ')
        aula = input('Digite o id da aula: ')
        curso = input('Digite o id do curso: ')
        anonimo = input('Digite SIM se o comentario for animo e NÂO para digitar seu nome: ')
        if anonimo == 'SIM':
            anonimo = True
        elif anonimo == 'NAO':
            anonimo = False
            nome = input('Digite seu nome: ')
            verificar_nome = session.query(Usuario).filter(Usuario.nome == nome).first()
            if not verificar_nome:
                print('Aluno não encontrado!')
                return
        aluno_id = verificar_nome.id
        comentario = Comentario(titulo=titulo, descricao=descricao, data_comentario=data_comentario, aula=aula, curso=curso, anonimo=anonimo, aluno=aluno_id)
        session.add(comentario)
        session.commit()
        print('Comentario cadastrado com sucesso!')

    def listar_comentario():
        print('--------------LISTAR COMENTARIO--------------')
        comentarios = session.query(Comentario).all()
        if not comentarios:
            print('Nenhum comentario cadastrado!')
        else:
            for c in comentarios:
                print(f'ID: {c.id}, Titulo: {c.titulo}, Descricao: {c.descricao}, Data: {c.data_comentario}, Aula: {c.aula}, Curso: {c.curso}, Anonimo: {c.anonimo}, Aluno: {c.aluno}')

    def editar_comentario():
        print('--------------EDITAR COMENTARIO--------------')
        id_comentario = input('Digite o id do comentario que deseja editar: ')
        comentario = session.query(Comentario).filter_by(id=id_comentario).first()
        if not comentario:
            print('Comentario não encontrado!')
            return
        else:
            titulo = input('Digite o novo titulo do comentario: ')
            descricao = input('Digite a nova descricao do comentario: ')
            data_comentario = input('Digite a nova data do comentario: ')
            comentario.titulo = titulo
            comentario.descricao = descricao
            comentario.data_comentario = data_comentario
            session.commit()
            print('Comentario editado com sucesso!')

    def excluir_comentario():
        print('--------------EXCLUIR COMENTARIO--------------')
        id = input('Digite o id do comentario que deseja excluir: ')
        comentario = session.query(Comentario).filter_by(id=id).first()
        if not comentario:
            print("Comentario não encotrado: ")
            return
        else:
            session.delete(comentario)
            session.commit()
            print("Comentario excluido com sucesso!")





