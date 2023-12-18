from HashTable import ChainingHashTable as HashTable
from Jogo import Jogo
import csv

class DataSet:
    #===============CONSTRUTOR===============================
    def __init__(self, csv_path : str):        
        self.__itens_descartados = 0
        self.__itens_carregados = 0

        csv = self.__carregar_csv(csv_path)
        len_csv = len(csv)

        self.__jogos = HashTable(len_csv)
        self.__sistemas_operacionais = HashTable(len_csv)
        self.__anos_de_lancamento = HashTable(len_csv)
        self.__povoar_tabelas(csv)

    # =================GETTERS===============================
    @property
    def jogos(self):
        return self.__jogos

    @property
    def descartados(self):
        return self.__itens_descartados

    @property
    def carregados(self):
        return self.__itens_carregados

    @property
    def sistemas_operacionais(self):
        return self.__sistemas_operacionais

    @property
    def so_com_mais_titulos(self):
        lista_de_so = self.sistemas_operacionais.keys()
        qtd_sistema = {}
        for i in lista_de_so:
            qtd_sistema[len(self.sistemas_operacionais[i])] = i
        return qtd_sistema[max(qtd_sistema)]

    @property
    def anos_de_lancamento(self):
        return self.__anos_de_lancamento


    #=============METODOS PUBLICOS====================================
    
    def add_jogo(self, row : list):
        try:
            jogo = Jogo(row)
        except AssertionError as ae:
            #print(ae)
            return
            
        if jogo.nome in self.__jogos:
            return False
        
        self.__jogos[jogo.nome] = jogo
        return jogo      

    def pesquisar_jogo(self, item : str) -> list:
        tabela_levenhstein = HashTable(self.carregados)    
        for i in self.jogos.keys():
            jogo = self.jogos[i]
            indice = self.__levenhstein(jogo.nome, item)
            
            if indice < 12:
                try:
                    tabela_levenhstein[indice].append(jogo)
                except KeyError:
                    tabela_levenhstein[indice] = [jogo]
        return tabela_levenhstein
            
    #=====================METODOS PRIVADADOS================
    
    def __carregar_csv(self, csv_path : str) -> list:
        with open(csv_path, "r") as file:
            csv_line_list = file.readlines()
            del csv_line_list[0]
            reader = csv.reader(csv_line_list)
        return list(reader)
            
    def __povoar_tabelas(self, csv : list) -> None:
        for game in csv:
            list(game)
            jogo = self.add_jogo(game)
            if not jogo:
                self.__itens_descartados += 1
                continue
                
            # Se já tiver o SO na HashTable, vai adicionar o jogo à lista do SO.
            # Caso não haja, vai criar a chave contendo a lista com um unico jogo.
            for sistema_operacional in jogo.sistemas_operacionais:
                try:
                    self.__sistemas_operacionais[sistema_operacional].append(jogo)
                except KeyError:
                    self.__sistemas_operacionais[sistema_operacional] = [jogo]
            try:
                self.__anos_de_lancamento[jogo.ano_lancamento].append(jogo)
            except KeyError:
                self.__anos_de_lancamento[jogo.ano_lancamento] = [jogo]

            self.__itens_carregados += 1

    def __levenhstein(self, str1, str2):
        '''
            retorna um numero inteiro que quanto maior, mais distante da string.
            o valor 1 representa o exato nome buscado.
        '''
        # Obtém o comprimento das duas strings
        len_str1 = len(str1)
        len_str2 = len(str2)
        
        # Inicializa uma matriz para armazenar as distâncias parciais
        dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    
        # Inicializa a primeira coluna da matriz
        for i in range(len_str1 + 1):
            dp[i][0] = i
    
        # Inicializa a primeira linha da matriz
        for j in range(len_str2 + 1):
            dp[0][j] = j
    
        # Preenche a matriz usando a fórmula de recorrência
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,       # Deletar
                    dp[i][j - 1] + 1,       # Inserir
                    dp[i - 1][j - 1] + cost  # Substituir
                )
        # O último valor na matriz contém a distância Levenshtein
        return dp[len_str1][len_str2]