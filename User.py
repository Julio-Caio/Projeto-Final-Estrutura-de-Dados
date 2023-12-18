import bcrypt

class User:
    def __init__(self, username: str):
        self.__username = username

    def __str__(self):
        return f'username: {self.__username}'

    @property
    def username(self):
        return self.__username