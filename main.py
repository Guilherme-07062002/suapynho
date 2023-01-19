from suap import *

app = Suapynho()

# Inserindo dados na tabela para realizar os testes:

# app.cadastrarAluno("Edson", 123456, "Edinho@gmail.com")
# app.cadastrarAluno("Jessie", 654321)
# app.cadastrarAluno("Bartolomeu", 102030)
#
# app.cadastrarDisciplina("Banco de Dados", 60)
# app.cadastrarDisciplina("POO", 80)
# app.cadastrarDisciplina("Sistemas Operacionais", 100)
""" app.matricularAluno(2, 1)
app.matricularAluno(2, 3)
app.matricularAluno(4, 2)
app.matricularAluno(4, 1)
app.matricularAluno(3, 3) """

while True:
    print('SUAPYNHO'.center(50, '-'))
    print("""
1 - Cadastrar Aluno
2 - Cadastrar Disciplina
3 - Matricular aluno em disciplina
4 - Listar disciplinas que aluno está matriculado
5 - Lista de chamada
6 - Sair
    """)

    opcao = int(input("Digite uma Opcao: "))

    if (opcao == 1):
        print('Cadastrar aluno'.center(30, '-'))
        sleep(1)
        nomeAluno = input("Nome do novo aluno: ")
        emailAluno = input("Email: ")
        matriculaAluno = int(input("Matricula: "))
        app.cadastrarAluno(nomeAluno, matriculaAluno, emailAluno)
    elif (opcao == 2):
        print('Cadastrar disciplina'.center(30, '-'))
        sleep(1)
        nomeDisciplina = input('Informe o nome da disciplina: ')
        carga_horaria = int(input('Informe a carga horária: '))
        app.cadastrarDisciplina(nomeDisciplina, carga_horaria)
    elif (opcao == 3):
        print('Matricular aluno'.center(30, '-'))
        sleep(1)
        id_aluno = int(input('Informe a id do aluno: '))
        id_disciplina = int(input('Informe a id da disciplina: '))
        app.matricularAluno(id_aluno, id_disciplina)
    elif (opcao == 4):
        print('Listar disciplinas do aluno'.center(30, '-'))
        sleep(1)
        matriculaAluno = int(input('Informe a matricula do aluno: '))
        app.listarDisciplinasAluno(matriculaAluno)
    elif (opcao == 5):
        print('Exibir lista de chamada'.center(30, '-'))
        sleep(1)
        id_disciplina = int(input('Informe a id da disciplina: '))
        app.listaChamada(id_disciplina)
    elif (opcao == 6):
        print('Bye')
        break
    else:
        print("\nOpcao Invalida. Tente de novo\n")
        sleep(2)
