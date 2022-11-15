import classes.Aluno as Aluno
import database.connection as Connection
import os


class App:

    def __init__(self):
        Connection.Connection().create_table()
        self.conexao = Connection.Connection()

    def __clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __cadastro_aluno(self):

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

    def __listar_alunos(self):
        result = Connection.Connection().select("SELECT * FROM alunos")

        for row in result:
            print("Nome: " + row[0])
            print("Rua: " + row[1])
            print("Número: " + row[2])
            print("Bairro: " + row[3])
            print("Cidade: " + row[4])
            print("UF: " + row[5])
            print("Telefone: " + row[6])
            print("Email: " + row[7])
            print("Matrícula: " + row[8])
            print("=====================================")

    def __remover_aluno(self):
        print("Remover aluno")
        matricula = input("Digite a matrícula do aluno: ")
        sql = "DELETE FROM alunos WHERE matricula = '{}'".format(matricula)
        Connection.Connection().delete(sql)

    def Welcome(self):
        print("Olá, seja bem vindo ao sistema de cadastro de alunos")
        print("O que deseja fazer?")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Remover aluno")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        self.__Menu(opcao)

    def __Menu(self, opcao):
        if opcao == 1:
            self.__clear()
            self.__cadastro_aluno()
            print("Aluno cadastrado com sucesso!")
            input("Pressione enter tecla para continuar...")
            self.__clear()
            return self.Welcome()

        elif opcao == 2:
            self.__clear()
            print("Listar alunos")
            self.__listar_alunos()
            input("Pressione enter tecla para continuar...")
            self.__clear()
            return self.Welcome()

        elif opcao == 3:
            self.__clear()
            self.__remover_aluno()
            input("Pressione enter tecla para continuar...")
            print("Aluno removido com sucesso!")
            self.__clear()
            return self.Welcome()

        elif opcao == 4:
            self.__clear()
            print("Saindo do sistema...")
            print("Obrigado por utilizar o sistema de cadastro de alunos 😁")
            print("Alunos participantes do projeto:")
            print(". João Gabriel Pinho da Cruz")
            print(". Gabriel Danny")
            print(". Thaynara Damazio")
            print(". Leonardo")
            exit()

        else:
            self.__clear()
            print("Opção inválida, tente novamente!")
            return self.Welcome()


App = App()

App.Welcome()
