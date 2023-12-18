import DataSet as DS
from User import User
from Database import Database
from Menu import Menu

if __name__ == "__main__":
    menu = Menu()
    email = input("Digite seu e-mail: ")

    print(f'''
    Bem-Vindo ao Gerenciador de Jogos, {email}! Como deseja entrar?
    ===================================
    | (1) Entrar com token de acesso   |
    ===================================
    | (2) Não autenticar por enquanto  |
    ====================================
    ''')

    database = Database()
    opcao = int(input('> Escolha sua opção de login: '))
    user = User(email)
    database.cadastrar(user, opcao)
    
    if opcao == 1:
        token = int(input("\nDigite o token de acesso: "))
        if database.validar_token(token):
            menu()
    
    elif opcao == 2:
        menu()

    else:
        print("Opção inválida!")
        exit()
