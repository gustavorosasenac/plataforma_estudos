from sqlalchemy import Column, String, Integer, Date, ForeignKey
from database.db_connections.db import Base, session

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    genero = Column(String)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    cidade = Column(String)
    estado = Column(String)
    pais = Column(String)
    cep = Column(String)

class Professor(Usuario):
    __tablename__ = 'professor'
    materias = Column(String)
    curso = Column(Integer, ForeignKey('curso.id'))
    aulas = Column(Integer, ForeignKey('aula.id'))

class Aluno(Usuario):
    __tablename__ = 'aluno'
    cursos = Column(Integer, ForeignKey('curso.id'))
    em_progresso = Column(Integer, ForeignKey('aula.id'))
    aulas = Column(Integer, ForeignKey('aula.id'))
    materias = Column(String)
    provas = Column(Integer, ForeignKey('prova.id'))

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

    if not all([nome, nascimento, email, telefone]):
        print("Preencha todos os campos obrigatórios!")
        return

    novo_aluno = Aluno(nome=nome,nascimento=nascimento,genero=genero,email=email,telefone=telefone,cidade=cidade,estado=estado,pais=pais,cep=cep)

    session.add(novo_aluno)
    session.commit()
    print("Aluno cadastrado com sucesso!")