from suap import *

app = Suapynho()

# app.cadastrarAluno("Edson", 123456, "Edinho@gmail.com")
# app.cadastrarAluno("Jessie", 654321)
# app.cadastrarAluno("Bartolomeu", 102030)
#
# app.cadastrarDisciplina("Banco de Dados", 60)
# app.cadastrarDisciplina("POO", 80)
# app.cadastrarDisciplina("Sistemas Operacionais", 100)

while True:
    print('SUAPYNHO'.center(50, '-'))
    print("""
1 - Cadastrar Aluno
2 - Cadastrar Disciplina
3 - Matricular aluno em disciplina
4 - Listar disciplinas
5 - Lista de chamada
6 - Sair
    """)
    opcao = int(input("Digite uma Opcao: "))
    if (opcao == 1):
        nomeAluno = input("Informe o nome do aluno: ")
        emailAluno = input("Informe o Email do aluno: ")
        matriculaAluno = int(input("Informa a Matricula do aluno: "))
        app.cadastrarAluno(nomeAluno, matriculaAluno, emailAluno)
    elif (opcao == 2):
        nomeDisciplina = input('Informe o nome da disciplina: ')
        carga_horaria = int(input('Informe a carga horária: '))
        app.cadastrarDisciplina(nomeDisciplina, carga_horaria)
    elif (opcao == 3):
        id_aluno = int(input('Informe a id do aluno: '))
        id_disciplina = int(input('Informe a id da disciplina: '))
        app.matricularAluno(id_aluno, id_disciplina)
    elif (opcao == 4):
        matriculaAluno = int(input('Informe a matricula do aluno: '))
        app.listarDisciplinasAluno(matriculaAluno)
    elif (opcao == 5):
        id_disciplina = int(input('Informe a id da disciplina: '))
        app.listaChamada(id_disciplina)
    elif (opcao == 6):
        print('Bye')
        break
    else:
        print("Opcao Invalida Doido. Tente de novo")
