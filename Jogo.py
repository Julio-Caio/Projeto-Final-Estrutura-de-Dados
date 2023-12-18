import re

class Jogo:
    #================CONSTRUTOR==========================
    def __init__(self, csv_row : list) -> None:
        self.__tratar_linha(csv_row)
        
        self.__nome = csv_row[0]
        self.__desenvolvedora = csv_row[1]
        self.__produtora = csv_row[2]
        self.__genero = self.__padronizar_genero(csv_row[3])
        self.__sistemas = self.__padronizar_sistema(csv_row[4])
        self.__dia = None
        self.__mes = None
        self.__ano = None
        self.__data = self.__padronizar_data(csv_row[5])

    #==============GETTERS=============================
    @property
    def nome(self):
        return self.__nome

    @property
    def sistemas_operacionais(self) -> list[str]:
        return self.__sistemas

    @property
    def dia_lancamento(self):
        return self.__dia

    @property
    def mes_lancamento(self):
        return self.__mes

    @property
    def ano_lancamento(self):
        return self.__ano

    @property
    def data_lancamento(self):
        return self.__data

    @property
    def genero(self):
        return self.list_to_string(self.__genero)

    @property
    def desenvolvedora(self):
        return self.__desenvolvedora

    #=============METODOS PRIVADOS=====================
    def __str__(self):
        return self.nome

    def __lt__(self, jogo : object):
        return self.__nome < jogo.nome

    def __eq__(self, jogo : object):
        return self.__nome == jogo.nome

    def __gt__(self, jogo : object):
        return self.__nome > jogo.nome

    def __tratar_linha(self, row) -> None:
        '''
        Tira os espaços em branco entre os campos e 
        assegura que não haverão campos vazios.
        '''
        for i in row:
            i.strip()
            assert i != "", "Não pode ter campo vazio."
    
    def __padronizar_genero(self, genero : str) -> list:
        # SÓ VAI ACEITAR OS PADRÕES DESCRITOS NO DICIONÁRIO.
        padroes = {
            "4X" : r"4x", 
            "Adventure" : r"adventure",
            "Action" : r"action",
            "Art" : r"art",
            "Arcade" : r"arcade",
            "Battle Royale" : r"battle\sroyale",
            "Co-op" : r"co.op",
            "RTS" : r"(real.time.(strategy)|(tactics))|(^rts$)",
            "FPS" : r"(fps)|(first.person.shooter)",
            "Eduacation" : r"(education)|(serious)",
            "Music" : r"music",
            "Simulation" : r"simulat",
            "Racing" : r"racing",
            "Sports" : r"(sports)|(soccer)",
            "Shooter" : r"shoot",
            "Strategy" : r"(strategy)|(tactical)",
            "MMO" : r"MMO",
            "RPG" : r"(role?.playing)|(rpg)",
            "Wargame" : r"war",
            "Fighting" : r"fight",
            "Novel" : r"(novel)|(fiction)",
            "Puzzle" : r"puzzle",
            "Platformer" : r"platform",
            "Stealth" : r"stealth",
            "City-building" : r"city.building",
            "Survival" : r"survival",
            "Horror" : r"(horror)|(terror)|(zombies)",
            "Moba" : r"moba",
            "Indie" : r"indie",
            "Sandbox" : r"sandbox",
            "Tycoon" : r"tycoon",
            "Pinball" : r"Pinball",
            "Open World" : r"open.world",
            "Incremental" : r"incremental",
            "god game" : r"god",
            "Exploration" : r"exploration",
            "Word" : r"word",
            "Compilation" : r"compilation",
            "Rogue Like" : r"rogue",
            "Mystery" : r"mystery",
            "Vehicular Combat" : r"vehicular.combat",
            "Reverse Tower" : r"reverse.tower"
        }

        lista = []
        for chave in padroes.keys():
            if re.search(padroes[chave], genero, flags=re.IGNORECASE):
                lista.append(chave)
        assert lista != [], "O genero não é valido."
        return lista

    def list_to_string(self, lista : list) -> str:
        l = len(lista)
        string = ""
        for i in range(l-1):
            string += lista[i] + "/" 
        string += lista[l-1]
        return string
        

    def __padronizar_sistema(self, sistema : str) -> list:
        padroes = {
            "Apple II" : r"apple\sii",
            "Atari" : r"atari",
            "Commodore" : r"(commodore)|(amiga)",
            "Mac" : r"(mac)|(os\sx)",
            "PC-98" : r"pc-98",
            "DOS" : "(dos)|(ibm)",
            "Windows" : r"windows",
            "Xbox" : r"xbox"
        }

        lista_os = []
        for chave in padroes.keys():
            if re.search(padroes[chave], sistema, flags=re.IGNORECASE):
                lista_os.append(chave)
        return [sistema] if lista_os == [] else lista_os

    def __padronizar_data(self, data : str) -> str:
        # Decidimos não incluir os jogos que 
        # não possuissem a data completa.
        lista_meses = { 
            'January': '01', 'February': '02', 'March': '03',
            'April': '04', 'May': '05', 'June': '06',
            'July': '07', 'August': '08', 'September': '09',
            'October': '10','November': '11','December': '12'
        }

        data = data.split()
        tam = len(data)

        assert tam > 2 and data[0] in lista_meses, "tamanho da data menor que 2"
        self.__mes = lista_meses[data[0]]
        self.__dia = data[1].removesuffix(',')
        self.__ano = data[2].removesuffix(';')
        
        return f'{self.__dia}/{self.__mes}/{self.__ano}'