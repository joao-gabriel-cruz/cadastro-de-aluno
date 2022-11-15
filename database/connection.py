import sqlite3


class Connection:
    def __init__(self):

        self.banco = sqlite3.connect('cadastro.db')

        self.connection = self.banco.cursor()

    def create_table(self):
        try:
            self.connection.execute(
                'CREATE TABLE IF NOT EXISTS alunos (nome TEXT, rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, uf TEXT, telefone TEXT, email TEXT, matricula TEXT)'
            )
            self.banco.close()
        except:
            print('Não foi possível criar a tabela')

    def insert(self, sql):
        try:
            self.connection.execute(sql)
            self.banco.commit()
            self.connection.close()
        except:
            print("Não foi possível cadastrar o aluno")

    def select(self, sql):
        try:
            self.connection.execute(sql)
            rows = self.connection.fetchall()
            return rows
        except:
            print("Não foi possível listar os alunos")

    def delete(self, sql):
        try:
            self.connection.execute(sql)

            self.banco.commit()
            self.connection.close()
        except:
            print("Não foi possível remover o aluno")
