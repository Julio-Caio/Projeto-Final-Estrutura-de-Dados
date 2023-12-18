from DataSet import DataSet

class Interface:
    def __init__(self):
        self.df = DataSet("computer_games.csv")
        self.__header_games = f'''\
{" "*3} {"Jogo":30} {"Genero":20} {"Desenvolvedor":30} {"Lançamento":11}
{"="*3} {"="*30} {"="*20} {"="*30} {"="*11}\
'''

    def __lim(self, string, l):
        s = ""
        l_string = len(string)
        if l_string < l:
            return string + (" " * (l - l_string))
        for i in range(l-3):
            s += string[i]
        s+="..."
        return s

    def listar_jogos(self):
        # Cabeçalho:
        print("Lista de jogos:\n")
        print(self.__header_games)

        arvore_de_jogos = self.df.jogos.values() 
        for i in range(self.df.carregados):
            jogo = arvore_de_jogos[i]
            print(f"{i + 1:03} {self.__lim(jogo.nome, 30)} {self.__lim(jogo.genero, 20)} {self.__lim(jogo.desenvolvedora, 30)} {self.__lim(jogo.data_lancamento, 11)}")

    def jogos_por_so(self):
        '''
            vai exibir uma lista com todos os jogos
            para cada so.
        '''
        for sistema_operacional in self.df.sistemas_operacionais.keys():
            print("\n\nResultado (so):", sistema_operacional, "\n")
            print(self.__header_games)
            
            for i in range(len(self.df.sistemas_operacionais[sistema_operacional])):
                jogo = self.df.sistemas_operacionais[sistema_operacional][i]
                print(f"{i + 1:03} {self.__lim(jogo.nome, 30)} {self.__lim(jogo.genero, 20)} {self.__lim(jogo.desenvolvedora, 30)} {self.__lim(jogo.data_lancamento, 11)}")


    def jogos_por_ano(self):
        '''
            vai exibir uma lista com todos os jogos
            separados por ano.
        '''
        for ano in self.df.anos_de_lancamento.keys():
            print("\n\nResultado (ano):", ano, "\n")
            print(self.__header_games)
            for i in range(len(self.df.anos_de_lancamento[ano])):
                jogo = self.df.anos_de_lancamento[ano][i]
                print(f"{i + 1:03} {self.__lim(jogo.nome, 30)} {self.__lim(jogo.genero, 20)} {self.__lim(jogo.desenvolvedora, 30)} {self.__lim(jogo.data_lancamento, 11)}")

    def so_com_mais_titulos(self):
        print("Sistema operacional com mais titulos: ", self.df.so_com_mais_titulos)

    def qtd_jogos_por_ano(self):
        for i in self.df.anos_de_lancamento.keys():
            print(i + ": " + str(len(self.df.anos_de_lancamento[i])))

    def qtd_descartados(self):
        print("Quantidade de itens descartados: ", self.df.descartados)

    def qtd_carregados(self):
        print("Quantidade de itens carregados:", self.df.carregados)

    def pesquisar_jogo(self):
        pesquisa = input("Pesquisa: ")
        lista_resultado = []
        tabela_levenshtein = self.df.pesquisar_jogo(pesquisa)
        i = 1
        ocorrencias = 0
        for indice in tabela_levenshtein.keys():
            for jogo in tabela_levenshtein[indice]:
                if self.__ocorrencia(pesquisa, jogo.nome):
                    ocorrencias += 1
                lista_resultado.append(f"{i + 1:03} {self.__lim(jogo.nome, 30)} {self.__lim(jogo.genero, 20)} {self.__lim(jogo.desenvolvedora, 30)} {self.__lim(jogo.data_lancamento, 11)}")
                i += 1

        print(f"Tipo da busca (l) Levenhstein (12) Ocorrencia da palavra: {ocorrencias}\n")
        print(self.__header_games)
        for i in lista_resultado:
            print(i)

    def __ocorrencia(self, ref, outro):
        if ref > outro:
            return False
        for char in range(len(ref)):
            if ref[char] != outro[char]:
                return False
        return True