import classes.Aluno as Aluno
import database.connection as Connection


class App:

    def __init__(self):
        Connection.Connection().create_table()
        self.conexao = Connection.Connection()

    def cadastro_aluno(self):

        nome = input("Digite o nome do aluno: ")
        rua = input("Digite o nome da rua: ")
        numero = input("Digite o número da casa: ")
        bairro = input("Digite o nome do bairro: ")
        cidade = input("Digite o nome da cidade: ")
        uf = input("Digite o nome do estado: ")
        telefone = input("Digite o número de telefone: ")
        email = input("Digite o email do aluno: ")
        aluno = Aluno.Aluno(nome, rua, numero, bairro,
                            cidade, uf, telefone, email)

        sql = "INSERT INTO alunos VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            aluno.get_nome(), aluno.get_rua(), aluno.get_numero(), aluno.get_bairro(), aluno.get_cidade(), aluno.get_uf(), aluno.get_telefone(), aluno.get_email(), aluno.get_matricula())

        Connection.Connection().insert(sql)

        print("Aluno cadastrado com sucesso!")

    def listar_alunos(self):

        Connection.Connection().select("SELECT * FROM alunos")

    def Welcome(self):
        print("Olá, seja bem vindo ao sistema de cadastro de alunos")
        print("O que deseja fazer?")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Remover aluno")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            self.cadastro_aluno()
            return self.Welcome()

        elif opcao == 2:
            print("Listar alunos")
            self.listar_alunos()
            return self.Welcome()


App = App()

App.Welcome()
