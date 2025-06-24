from models.curso import Curso
from database.db_connections.db import Base, engine

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
                    Curso.cadastrar_curso()
                case "2":
                    Curso.listar_curso()
                case "3":
                    Curso.alterar_curso()
                case "4":
                    Curso.excluir_curso()
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
                    from models.usuario import cadastro_aluno
                    cadastro_aluno()
                case "2":
                    from models.usuario import listar_alunos
                    listar_alunos()
                case "3":
                    from models.usuario import alterar_aluno
                    alterar_aluno()
                case "4":
                    from models.usuario import excluir_aluno
                    excluir_aluno()
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


        

        
