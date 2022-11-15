from datetime import datetime


class Aluno:

    def __init__(self, nome, rua, numero, bairro, cidade, uf, telefone, email,):
        self.__nome = nome
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf
        self.__telefone = telefone
        self.__email = email
        self.__matricula = datetime.now().strftime("%Y%m%d%H%M%S")

    def get_nome(self):
        return self.__nome

    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self.__bairro

    def get_cidade(self):
        return self.__cidade

    def get_uf(self):
        return self.__uf

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_matricula(self):
        return self.__matricula
