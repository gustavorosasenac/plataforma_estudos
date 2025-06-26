from sqlalchemy import Column, String, Integer, Date, ForeignKey
from database.db_connections.db import Base, session

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    nascimento = Column(Date, nullable=False)
    genero = Column(String(100))
    email = Column(String(100), nullable=False)
    telefone = Column(String(100), nullable=False)
    cidade = Column(String(100))
    estado = Column(String(100))
    pais = Column(String(50))
    cep = Column(String(30))

'''class Professor(Usuario):
    __tablename__ = 'professor'
    materias = Column(String)
    #curso = Column(Integer, ForeignKey('curso.id'))
    #aulas = Column(Integer, ForeignKey('aula.id'))'''

class Aluno(Usuario):
    __tablename__ = 'aluno'
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    #cursos = Column(Integer, ForeignKey('curso.id'))
    #em_progresso = Column(Integer, ForeignKey('aula.id'))
    #aulas = Column(Integer, ForeignKey('aula.id'))
    materias = Column(String(200))
    #provas = Column(Integer, ForeignKey('prova.id'))

    def cadastro_aluno():
        print("---------CADASTRO DE ALUNO---------")
        nome = input("Digite o nome do aluno: ")
        nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
        genero = input("Digite o gênero do aluno: ")
        email = input("Digite o email do aluno: ")
        telefone = input("Digite o telefone do aluno: ")
        cidade = input("Digite a cidade do aluno: ")
        estado = input("Digite o estado do aluno: ")
        pais = input("Digite o país do aluno: ")
        cep = input("Digite o CEP do aluno: ")
        materias = input("Digite as materias do aluno")

        if not all([nome, nascimento, email, telefone]):
            print("Preencha todos os campos obrigatórios!")
            return

        novo_aluno = Aluno(nome=nome,nascimento=nascimento,genero=genero,email=email,telefone=telefone,cidade=cidade,estado=estado,pais=pais,cep=cep,materias=materias)

        session.add(novo_aluno)
        session.commit()
        print("Aluno cadastrado com sucesso!")
    
    def listar_aluno():
        print("-------------LISTA DE ALUNOS-------------")
        alunos = session.query(Aluno).all()
        if not alunos:
            print("Nenhum aluno cadastrado!")
        else:
            for a in alunos:
                print(f"ID: {a.id}, Nome: {a.nome}, Nascimento: {a.nascimento}, Genero: {a.genero}, E-mail: {a.email}, Telefone: {a.telefone}, Cidade: {a.cidade}, Estado: {a.estado}, Pais: {a.pais}, CEP: {a.cep}, Materias: {a.materias}" )
                return
            
    def alterar_aluno():
        print("------------ALTERAR ALUNO------------")
        id = input("Digite o ID do aluno que deseja alterar: ")
        verificar = session.query(Aluno).filter(Aluno.id == id).first()
        if not verificar:
            print("Aluno não encontrado")
        else:
            nome = input("Digite o nome do aluno: ")
            nascimento= input("Digite a data de nascimento do aluno: ")
            genero = input("Digite o genero do aluno: ")
            email = input("Digite o E-mail do aluno: ")
            telefone = input("Digite o telefone do aluno")
            cidade = input("Digite a cidade do aluno: ")
            estado = input("Digite o estado do aluno: ")
            pais = input("Digite o pais do aluno: ")
            cep = input("Digite o CEP do aluno: ")
            materias = input("Digite as materias do aluno: ")
            if not all([nome, nascimento, genero, email, telefone, cidade, estado, pais, cep, materias]):
                print("Preencha todos os campos")
                return
            else:
                verificar.nome = nome
                verificar.nascimento
                verificar.genero = genero
                verificar.email = email
                verificar.telefone = telefone
                verificar.cidade = cidade
                verificar.estado = estado
                verificar.pais = pais
                verificar.cep = cep
                verificar.materias = materias
                session.commit()
                print("Informações do aluno atualizadas!")

    def excluir_aluno():
        print("-------------EXCLUIR CURSO-------------")
        id = input("Digite o id do curso que deseja excluir: ")
        verificar = session.query(Aluno).filter(Aluno.id == id).first()
        if not verificar:
            print("Aluno não encontrado!")
        else:
            session.delete(verificar)
            session.commit()
        