from Interface import Interface as Manager

class Menu:
    def __init__(self):
        self.__manager = Manager()
        
    def __str__(self):
        return '''
        ============= Menu Principal ==============
        (l) Listar jogos por sistema operacional
        (p) Pesquisar jogo
        (d) Listar jogos por ano de lançamento
        (s) Sair
        (o) Outras opções
        '''

    def __functions(self, key):
        key = key.lower()
    
        functions = {
            'l': self.__manager.jogos_por_so,
            'p': self.__manager.pesquisar_jogo,
            'd': self.__manager.jogos_por_ano,
            's': exit,
            'o': {
                "1": self.__manager.listar_jogos,
                "2": self.__manager.qtd_jogos_por_ano
            }
        }
    
        if key in functions and key != 'o':
            function = functions[key]
            self.__getParams(function)
    
        elif key == 'o':
            print('''
                  Opções Avançadas
            ======================================
                (1) Listar todos os jogos
                (2) Listar Qtde de Jogos p/ano
            ''')
    
            opcao_avancada = input("> Escolha uma das opções apresentadas: ")
            if opcao_avancada in functions['o']:
                function = functions['o'][opcao_avancada]
                self.__getParams(function)
            else:
                print("Não existe essa opção")
    
        else:
            print('Opção inválida')
            self.__call__()

    def __getParams(self, function):
        if function == Manager.jogos_por_so:
            parametro = input("> Pesquisar Sistema operacional: ")
            function(parametro)
        elif function == Manager.pesquisar_jogo:
            parametro = input("> Pesquisar Jogo: ")
            function(parametro)
        else:
            function()

    def __call__(self):
        while True:
            print(self)
            opcao = input("> Escolha uma opção: ")
            self.__functions(opcao)