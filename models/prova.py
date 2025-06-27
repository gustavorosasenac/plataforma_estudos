import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database.db_connections.db import session, Base

class Prova(Base):
    __tablename__ = 'prova'
    id = Column(Integer, primary_key=True, autoincrement=True)
    curso = Column(Integer, ForeignKey('curso.id'), nullable=True)
    material = Column(Integer, ForeignKey('material.id'), nullable=True)
    titulo = Column(String(25), nullable=False)
    descricao = Column(String(500))
    nota = Column(String(500))
    questoes = Column(Integer, ForeignKey('questoes.id'), nullable=True)

class Questao(Base):
    __tablename__ = 'questoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String(500))
    resposta = Column(String(500))
    resposta_correta = Column(String(500))

class OperacoesProva(Prova):
    def cadastrar_prova():
        print("------------CADASTRO DE PROVA------------")
        curso = input("Digite o ID do curso: ")
        titulo = input("Digite o titulo da prova: ")
        descricao = input("Digite a descrição da prova: ")
        nota = input("Digite a nota da prova: ")

        if not all([curso, titulo, descricao, nota]):
            print("Preencha todos os campos!")
        else:
            nova_prova = Prova(curso=curso, titulo=titulo, descricao=descricao, nota=nota)
            session.add(nova_prova)
            session.commit()
            print("Prova cadastrada com sucesso!")
            return
        
    def listar_prova():
        print("------------LISTA DE PROVAS------------")
        provas = session.query(Prova).all()
        if not provas:
            print("Nenhuma prova cadastrada!")
        else:
            for p in provas:
                print(f"ID: {p.id}, Curso: {p.curso}, Titulo: {p.titulo}, Descrição: {p.descricao}, Nota: {p.nota}")
            return
        
    def alterar_prova():
        print("------------ALTERAR PROVA------------")
        id_prova = input("Digite o ID da prova que deseja alterar: ")
        prova = session.query(Prova).filter(Prova.id == id_prova).first()
        
        if not prova:
            print("Prova não encontrada!")
            return
        
        titulo = input("Digite o novo titulo da prova: ")
        descricao = input("Digite a nova descrição da prova: ")
        nota = input("Digite a nova nota da prova: ")

        if not all([titulo, descricao, nota]):
            print("Preencha todos os campos!")
        else:
            prova.titulo = titulo
            prova.descricao = descricao
            prova.nota = nota
            session.commit()
            print("Prova alterada com sucesso!")
            return
        
    def excluir_prova():
        print("------------EXCLUIR PROVA------------")
        id_prova = input("Digite o ID da prova que deseja excluir: ")
        prova = session.query(Prova).filter(Prova.id == id_prova).first()
        
        if not prova:
            print("Prova não encontrada!")
            return
        
        session.delete(prova)
        session.commit()
        print("Prova excluída com sucesso!")
        return
    

