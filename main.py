

class App:
    def Welcome(self):
        print("Olá, seja bem vindo ao sistema de cadastro de alunos")
        print("O que deseja fazer?")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            print("Cadastrar aluno")


App = App()

App.Welcome()
