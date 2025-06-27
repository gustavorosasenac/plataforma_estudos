from sqlalchemy import Column, String, Integer, Date, ForeignKey
from database.db_connections.db import Base, session

class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    materia = Column(String(100))
    formato = Column(String(5))
    caminho_arquivo = Column(String(100))
    aula = Column(Integer, ForeignKey('aula.id'), nullable=True)

class OperacoesMaterial(Material):
    def cadastrar_material():
        print("------------CADASTRO DE MATERIAIS------------")
        nome = input("Digite o nome do material: ")
        materia = input("Digite a materia do material: ")
        formato = input("Digite o formato do material: ")
        if not all ([nome, materia, formato]):
            print("Preencha todos os campos")
            return
        else:
            novo_material = Material(nome=nome, materia=materia, formato=formato)
            session.add(novo_material)
            session.commit()
            print("Material cadastrado com sucesso!")

    def listar_materiais():
        print("------------LISTA DE MATERIAIS------------")
        materiais = session.query(Material).all()
        if materiais:
            for m in materiais:
                print(f"ID: {m.id}, Nome: {m.nome}, Materia: {m.materia}, Formato: {m.formato}")
        else:
            print("Nenhum material encontrado.")

    def editar_material():
        print("------------EDITAR MATERIAIS------------")
        id = int(input("Digite o ID do material que deseja editar: "))
        material = session.query(Material).filter_by(id=id).first()
        if material:
            print(f"ID: {material.id}, Nome: {material.nome}, Materia: {material.materia}, Formato: {material.formato}")
            nome = input("Digite o novo nome do material: ")
            materia = input("Digite a nova materia do material: ")
            formato = input("Digite o novo formato do material: ")
            material.nome = nome
            material.materia = materia
            material.formato = formato
            session.commit()
            print("Material editado com sucesso!")
        else:
            print("Material não encontrado.")

    def excluir_material():
        print("------------EXCLUIR MATERIAIS------------")
        id = int(input("Digite o ID do material que deseja excluir: "))
        material = session.query(Material).filter_by(id=id).first()
        if material:
            session.delete(material)
            session.commit()
            print("Material excluído com sucesso!")
        else:
            print("Material não encontrado.")






        
        

        


