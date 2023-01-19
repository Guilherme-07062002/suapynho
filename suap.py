import mysql.connector
from time import sleep

# Criando classe Banco
class Suapynho:
    # Configurando método construtor
    def __init__(self):
        conf = {
            "host": "localhost",
            "user": "gui",
            "password": "12345"
        }

        # Estabelecendo conexão com o banco de dados
        self.conexao = mysql.connector.connect(**conf)
        self.cursor = self.conexao.cursor()

        # Criando base de dados
        sql_criarBanco = '''CREATE DATABASE IF NOT EXISTS suapynho'''
        self.cursor.execute(sql_criarBanco)
        self.cursor.execute('USE suapynho')

        # Criando tabela alunos
        sql_criarAluno = '''CREATE TABLE IF NOT EXISTS alunos(
                                    id integer auto_increment,
                                    nome varchar(22) not null,
                                    matricula integer not null unique,
                                    email varchar(50),
                                    primary key(id)
                                    )'''
        self.cursor.execute(sql_criarAluno)

        # Criando tabela disciplinas
        sql_criarDisciplina = '''CREATE TABLE IF NOT EXISTS disciplinas(
                                           id integer auto_increment,
                                           nome varchar(22) not null,
                                           carga_horaria integer not null,
                                           primary key(id)
                                           )'''
        self.cursor.execute(sql_criarDisciplina)

        # Criando tabela matriculas
        sql_criarMatricula = '''CREATE TABLE IF NOT EXISTS matriculas(
                                                   id integer auto_increment,
                                                   id_aluno integer not null,
                                                   id_disciplina integer not null,
                                                   primary key(id),
                                                   foreign key (id_aluno) references alunos(id),
                                                   foreign key (id_disciplina) references disciplinas(id)
                                                   )'''
        self.cursor.execute(sql_criarMatricula)

    def cadastrarAluno(self, nome, matricula, email=''):
        sql = '''INSERT INTO alunos (nome, matricula, email) 
        VALUES(%s, %s, %s)'''
        self.cursor.execute(sql, (nome, matricula, email))
        self.conexao.commit()

    def cadastrarDisciplina(self, nome, carga_horaria):
        sql = '''INSERT INTO disciplinas (nome, carga_horaria)
        VALUES(%s, %s)'''
        self.cursor.execute(sql, (nome, carga_horaria))
        self.conexao.commit()

    def matricularAluno(self, id_aluno, id_disciplina):
        sql = '''INSERT INTO matriculas (id_aluno, id_disciplina)
        VALUES(%s, %s)'''
        self.cursor.execute(sql, (id_aluno, id_disciplina))
        self.conexao.commit()

    def listarDisciplinasAluno(self, matricula_aluno):
        sql = 'SELECT id FROM alunos where matricula = %s'
        self.cursor.execute(sql, (matricula_aluno, ))
        id = self.cursor.fetchall()
        sql2 = 'SELECT id_disciplina from matriculas where id_aluno = %s'
        self.cursor.execute(sql2, (id[0][0], ))
        resultado = self.cursor.fetchall()
        ids_disciplinas = []
        for elemento in resultado:
            ids_disciplinas.append(elemento[0])
        # print(ids_disciplinas)
        sql3 = 'SELECT nome FROM disciplinas where id = %s'
        sql4 = 'SELECT nome FROM alunos WHERE matricula = %s'
        self.cursor.execute(sql4, (matricula_aluno, ))
        nome = self.cursor.fetchall()[0][0]
        print(f'\nO aluno {nome} está matriculado nas disciplinas: ')
        for disciplina in ids_disciplinas:
            self.cursor.execute(sql3, (disciplina, ))
            print(' - ', self.cursor.fetchall()[0][0])
        sleep(3)
        print('')
        

    def listaChamada(self, id_disciplina):
        sql = 'SELECT id_aluno FROM matriculas WHERE id_disciplina = %s'
        self.cursor.execute(sql, (id_disciplina, ))
        res = self.cursor.fetchall()
        id_alunos = []
        sql2 = 'SELECT nome FROM alunos WHERE id = %s'
        for element in res:
            id_alunos.append(element[0])
        sql3 = 'SELECT nome FROM disciplinas WHERE id = %s'
        self.cursor.execute(sql3, (id_disciplina , ))
        nomeDisciplina = self.cursor.fetchall()[0][0]
        print(f'\nAlunos matriculados na disciplina {nomeDisciplina}:')
        for aluno in id_alunos:
            self.cursor.execute(sql2, (aluno, ))
            print(' - ', self.cursor.fetchall()[0][0])
        sleep(3)
        print('')

