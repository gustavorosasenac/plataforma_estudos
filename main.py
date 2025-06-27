from models.curso import OperacoesCurso
from database.db_connections.db import Base, engine
from models.usuario import Aluno, Professor
from models.aula import OperacoesAulas
from models.prova import OperacoesProva
from models.material import OperacoesMaterial
from models.comentario import OperacoesComentario


Base.metadata.create_all(engine)

while True:

    print("\n-------------------MENU-------------------")
    print("Digite SAIR para Sair do programa\n\n"
    "Digite 1 para CURSOS\n"
    "Digite 2 para ALUNOS\n"
    "Digite 3 para PROFESSORES\n"
    "Digite 4 para AULAS\n"
    "Digite 5 para PROVAS\n"
    "Digite 6 para MATERIAL\n"
    "Digite 7 para COMENTARIO\n")

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
            print("\n-----------------PROFESSORES-----------------\n")
            print("Digite 1 para cadastrar um Professor\n"
                  "Digite 2 para listar os Professores\n"
                  "Digite 3 para editar um Professor\n"
                  "Digite 4 para excluir um Professor\n"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    Professor.cadastro_professor()
                case "2":
                    Professor.listar_professor()
                case "3":
                    Professor.alterar_professor()
                case "4":
                    Professor.excluir_professor()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")
        
        case "4":
            print("\n-----------------AULAS-----------------\n")
            print("Digite 1 para cadastrar uma aula\n"
                  "Digite 2 para listar as aulas\n"
                  "Digite 3 para editar uma aula\n"
                  "Digite 4 para excluir uma aula\n"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    OperacoesAulas.cadastrar_aula()
                case "2":
                    OperacoesAulas.listar_aula()
                case "3":
                    OperacoesAulas.alterar_aula()
                case "4":
                    OperacoesAulas.excluir_aula()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")
        case "5":
            print("\n-----------------PROVAS-----------------\n")
            print("Digite 1 para cadastrar uma prova\n"
                  "Digite 2 para listar as provas\n"
                  "Digite 3 para editar uma prova\n"
                  "Digite 4 para excluir uma prova\n"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    OperacoesProva.cadastrar_prova()
                case "2":
                    OperacoesProva.listar_prova()
                case "3":
                    OperacoesProva.alterar_prova()
                case "4":
                    OperacoesProva.excluir_prova()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")
        case "6":
            print("\n-----------------MATERIAL-----------------\n")
            print("Digite 1 para cadastrar um material\n"
                  "Digite 2 para listar os materiais\n"
                  "Digite 3 para editar um material\n"
                  "Digite 4 para excluir um material\n"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    OperacoesMaterial.cadastrar_material()
                case "2":
                    OperacoesMaterial.listar_materiais()
                case "3":
                    OperacoesMaterial.editar_material()
                case "4":
                    OperacoesMaterial.excluir_material()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")
        case "7":
            print("\n-----------------COMENTARIO-----------------\n")
            print("Digite 1 para cadastrar um comentario\n"
                  "Digite 2 para listar os comentarios\n"
                  "Digite 3 para editar um comentario\n"
                  "Digite 4 para excluir um comentario"
                  "Digite SAIR para sair do menu")

            nova_opcao = input("Digite a opção desejada: ")

            match nova_opcao:
                case "1":
                    OperacoesComentario.cadastrar_comentario()
                case "2":
                    OperacoesComentario.listar_comentario()
                case "3":
                    OperacoesComentario.editar_comentario()
                case "4":
                    OperacoesComentario.excluir_comentario()
                case "SAIR":
                    break
                case _:
                    print("opção invalida!")





        case "SAIR":
            print("Saindo...")
            break
        case _:
            print("Opção invalida, tente novamente.")


        

        
