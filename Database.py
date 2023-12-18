from HashTable import ChainingHashTable as Ht
from random import randint
from User import User

class Database:
    def __init__(self):
        self.__database = Ht()
        self.__token = self.__generateToken()

    def __generateToken(self):
        token = randint(1, 10)
        while token in self.__database.values():
            token = randint(1, 100)
        return token

    @property
    def token(self):
        return self.__token

    def __cadastrarPorToken(self):
        try:
            self.__database.put(self.__user.username, self.__token)
            print("Status (204) - Created!")
            print('Seu token de acesso é: ', self.__token)

            return True
        except Exception as e:
            print(f"500 - Houve um problema com o nosso servidor, retorne mais tarde. Detalhes: {e}")
            return False

    def cadastrar(self, user, registration_type):
        self.__user = user
        if registration_type == 1:
            return self.__cadastrarPorToken()
        elif registration_type == 2:
            return True
        
    def validar_token(self, token):
        return token in self.__database.values()