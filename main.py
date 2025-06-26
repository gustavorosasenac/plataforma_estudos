from models.curso import OperacoesCurso
from database.db_connections.db import Base, engine
from models.usuario import Aluno


Base.metadata.create_all(engine)

while True:

    print("\n-------------------MENU-------------------")
    print("Digite SAIR para Sair do programa\n\n"
    "Digite 1 CURSOS\n"
    "Digite 2 ALUNOS\n"
    "Digite 3 PROFESSORES")

    opcao = input("\nDigite a opção desejada: ")

    match opcao:

        case "1":
            print("\n-----------------CURSOS-----------------\n")
            print("Digite 1 para cadastrar um curso\n"
                  "Digite 2 para listar os cursos\n"
                  "Digite 3 para editar um curso\n"
                  "Digite 4 para excluir um curso\n"
                  "Digite SAIR para sair do menu")
            
            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    OperacoesCurso.cadastrar_curso()
                case "2":
                    OperacoesCurso.listar_curso()
                case "3":
                    OperacoesCurso.alterar_curso()
                case "4":
                    OperacoesCurso.excluir_curso()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")

        case "2":

            print("\n-----------------ALUNOS-----------------\n")
            print("Digite 1 para cadastrar um aluno\n"
                  "Digite 2 para listar os alunos\n"
                  "Digite 3 para editar um aluno\n"
                  "Digite 4 para excluir um aluno\n"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    Aluno.cadastro_aluno()
                case "2":
                    Aluno.listar_aluno()
                case "3":
                    Aluno.alterar_aluno()
                case "4":
                    Aluno.excluir_aluno()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")

        case "3":
            pass
        


        case "SAIR":
            print("Saindo...")
            break
        case _:
            print("Opção invalida, tente novamente.")


        

        
