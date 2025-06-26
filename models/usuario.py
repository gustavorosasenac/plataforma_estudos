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

class Professor(Usuario):
    __tablename__ = 'professor'
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    materias = Column(String(200))
    #curso = Column(Integer, ForeignKey('curso.id'))
    #aulas = Column(Integer, ForeignKey('aula.id'))

    def cadastro_professor():
        print("---------CADASTRO DE PROFESSOR---------")
        nome = input("Digite o nome do professor: ")
        nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ")
        genero = input("Digite o gênero do professor: ")
        email = input("Digite o email do professor: ")
        telefone = input("Digite o telefone do professor: ")
        cidade = input("Digite a cidade do professor: ")
        estado = input("Digite o estado do professor: ")
        pais = input("Digite o país do professor: ")
        cep = input("Digite o CEP do professor: ")
        materias = input("Digite as materias do professor: ")

        if not all([nome, nascimento, email, telefone]):
            print("Preencha todos os campos obrigatórios!")
            return

        novo_professor = Professor(nome=nome,nascimento=nascimento,genero=genero,email=email,telefone=telefone,cidade=cidade,estado=estado,pais=pais,cep=cep,materias=materias)

        session.add(novo_professor)
        session.commit()
        print("Professor cadastrado com sucesso!")
    
    def listar_professor():
        print("-------------LISTA DE PROFESSORES-------------")
        professores = session.query(Professor).all()
        if not professores:
            print("Nenhum professor cadastrado!")
        else:
            for p in professores:
                print(f"ID: {p.id}, Nome: {p.nome}, Nascimento: {p.nascimento}, Genero: {p.genero}, E-mail: {p.email}, Telefone: {p.telefone}, Cidade: {p.cidade}, Estado: {p.estado}, Pais: {p.pais}, CEP: {p.cep}, Materias: {p.materias}" )
                return
            
    def alterar_professor():
        print("------------ALTERAR PROFESSOR------------")
        id = input("Digite o ID do professor que deseja alterar: ")
        verificar = session.query(Professor).filter(Professor.id == id).first()
        if not verificar:
            print("Professor não encontrado")
        else:
            nome = input("Digite o nome do professor: ")
            nascimento= input("Digite a data de nascimento do professor: ")
            genero = input("Digite o genero do professor: ")
            email = input("Digite o E-mail do professor: ")
            telefone = input("Digite o telefone do aprofessor")
            cidade = input("Digite a cidade do professor: ")
            estado = input("Digite o estado do professor: ")
            pais = input("Digite o pais do professor: ")
            cep = input("Digite o CEP do professor: ")
            materias = input("Digite as materias do professor: ")
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
                print("Informações do professor atualizadas!")

    def excluir_professor():
        print("-------------EXCLUIR PROFESSOR-------------")
        id = input("Digite o id do professor que deseja excluir: ")
        verificar = session.query(Professor).filter(Professor.id == id).first()
        if not verificar:
            print("Professor não encontrado!")
        else:
            session.delete(verificar)
            session.commit()

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
        id = input("Digite o id do aluno que deseja excluir: ")
        verificar = session.query(Aluno).filter(Aluno.id == id).first()
        if not verificar:
            print("Aluno não encontrado!")
        else:
            session.delete(verificar)
            session.commit()
        