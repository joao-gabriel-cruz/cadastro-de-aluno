import sqlite3


class Connection:
    def __init__(self):

        self.banco = sqlite3.connect('cadastro.db')

        self.connection = self.banco.cursor()

    def create_table(self):
        self.connection.execute(
            'CREATE TABLE IF NOT EXISTS alunos (nome TEXT, rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, uf TEXT, telefone TEXT, email TEXT, matricula TEXT)'
        )
        self.connection.close()

    def insert(self, sql):
        self.connection.execute(sql)
        self.banco.commit()
        self.connection.close()

    def select(self, sql):
        self.connection.execute(sql)
        rows = self.connection.fetchall()
        return rows

    def delete(self, sql):
        self.connection.execute(sql)
        self.banco.commit()
        self.connection.close()
