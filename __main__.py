import DataSet as DS
from User import User
from Database import Database
from Menu import Menu

if __name__ == "__main__":
    menu = Menu()

    print(f'''
    Bem-Vindo ao Gerenciador de Jogos! Como deseja entrar?
    ===================================
    | (1) Entrar com token de acesso   |
    ===================================
    | (2) Não autenticar por enquanto  |
    ====================================
    ''')

    database = Database()
    opcao = int(input('> Escolha sua opção de login: '))
    
    if opcao == 1:
        email = input("Digite seu e-mail: ")
        user = User(email)
        database.cadastrar(user, opcao)

        token = int(input("\nDigite o token de acesso: "))
        if database.validar_token(token):
            menu()
    
    elif opcao == 2:
        menu()

    else:
        print("Opção inválida!")
        exit()
