from sqlalchemy import Column, String, Integer, ForeignKey
from database.db_connections.db import Base, session

class Aulas(Base):
    __tablename__ = 'aula'
    id = Column(Integer, primary_key=True, autoincrement=True)
    professor = Column(Integer, ForeignKey('professor.id'), nullable=True)
    titulo = Column(String(100))
    materia = Column(String(100))
    check_in = Column(String(100))
    #comentarios = Column(ForeignKey('comentario.id'), nullable=True)
    material = Column(ForeignKey('material.id'), nullable=True)
    provas = Column(Integer, ForeignKey('prova.id'), nullable=True)

class OperacoesAulas(Aulas):

    def cadastrar_aula():
        print("------------CADASTRO DE AULA------------")
        professor = input("Digite o nome do professor: ")
        titulo = input("Digite o titulo da aula: ")
        materia = input("Digite a materia: ")
        check_in = input("Digite o inicio da aula: ")

        if not all ([titulo, materia, check_in]):
            print("Preencha todos os campos!")
        else:
            verificar = session.query(Aulas).filter(Aulas.professor == professor, Aulas.titulo == titulo, Aulas.materia == materia, Aulas.check_in == check_in).first()
            if verificar:
                print("Aula ja cadastrada!")
            else:
                nova_aula = Aulas(professor=professor, titulo=titulo, materia=materia, check_in=check_in)
                session.add(nova_aula)
                session.commit()
                print("Aula cadastrada com sucesso!")
                return
    
    def listar_aula():
        print("------------LISTA DE AULAS------------")
        aulas = session.query(Aulas).all()
        if not aulas:
            print("Nenhuma aula cadastrada!")
        else:
            for a in aulas:
                print(f"ID: {a.id}, Professor: {a.professor}, Titulo: {a.titulo}, Materia: {a.materia}, Check-in: {a.check_in}")
            return
    
    def alterar_aula():
        print("------------ALTERAR DE AULA------------")
        id_aula = input("Digite o ID da aula que deseja alterar: ")
        aula = session.query(Aulas).filter(Aulas.id == id_aula).first()
        
        if not aula:
            print("Aula não encontrada!")
            return
        
        titulo = input("Digite o novo titulo da aula: ")
        materia = input("Digite a nova materia: ")
        check_in = input("Digite o novo inicio da aula: ")

        if not all([titulo, materia, check_in]):
            print("Preencha todos os campos!")
        else:
            aula.titulo = titulo
            aula.materia = materia
            aula.check_in = check_in
            session.commit()
            print("Aula alterada com sucesso!")
        
    def excluir_aula():
        print("------------EXCLUIR AULA------------")
        id_aula = input("Digite o ID da aula que deseja excluir: ")
        aula = session.query(Aulas).filter(Aulas.id == id_aula).first()
        
        if not aula:
            print("Aula não encontrada!")
            return
        
        session.delete(aula)
        session.commit()
        print("Aula excluida com sucesso!")

    


