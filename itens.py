# cat = categoria, 0 = item, 1 = arma, 2 = armadura para diferenciar dentro do inventario do personagem

# para alvo, 0 = sem alvo,1= voce, 2 = inimigo 
# para tipo, 0= dano, 1= cura, 3= condição, 4= casos especiais

listaItens = [
    {
        'id': 0,
        'cat': 0,
        'nome': "poção de cura menor",
        'usavel': True,
        'tipo': 1,
        'tipoDano': None,
        'add': None,
        'alvo': 1,
        'valor': 20,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 1,
        'cat': 0,
        'nome': "frasco de acido menor",
        'usavel': True,
        'tipo': 2,
        'tipoDano': 8,
        'add': None,
        'alvo': 2,
        'valor': 20,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 2,
        'cat': 0,
        'nome': "poção de cura",
        'usavel': True,
        'tipo': 1,
        'tipoDano': None,
        'add': None,
        'alvo': 1,
        'valor': 50,
        'valorAdd': None,
        'desc': "frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 3,
        'cat': 0,
        'nome': "poção de cura maior",
        'usavel': True,
        'tipo': 1,
        'tipoDano': None,
        'add': None,
        'alvo': 1,
        'valor': 100,
        'valorAdd': None,
        'desc': "grande frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 4,
        'cat': 0,
        'nome': "chave antiga",
        'usavel': False,
        'tipo': 4,
        'tipoDano': None,
        'add': None,
        'alvo': 0,
        'valor': None,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 5,
        'cat': 0,
        'nome': "poção da meia morte ",
        'usavel': True,
        'tipo': 0,
        'tipoDano': 7,
        'add': None,
        'alvo': 1,
        'valor': 50,
        'valorAdd': None,
        'desc': "pequena frasco de liquido escuro, drena vitalidade"
    },
{
        'id': 6,
        'cat': 0,
        'nome': "poção da morte ",
        'usavel': True,
        'tipo': 0,
        'tipoDano': 7,
        'add': None,
        'alvo': 1,
        'valor': 500,
        'valorAdd': None,
        'desc': "Não beba isso"
    }
]
# tipos de dano
# 0 - impacto
# 1 - corte
# 2 - perfuração
# 3 - fogo
# 4 - raio
# 5 - veneno
# 6 - frio
# 7 - morte
# 8 - omnipotente
listaArmas = [
    {
        'id': 0,
        'cat': 1,
        'nome': "espada quebrada",
        'dano': 1,
        'hit': 65,
        'tipo': 1,
        'desc': "uma espada em pedaços, somente melhor doque nada"
    },
    {
        'id': 1,
        'cat': 1,
        'nome': "espada curta",
        'dano': 3,
        'hit': 85,
        'tipo': 1,
        'desc': "uma curta lamina de qualidade media, uma arma confiavel"
    },
    {
        'id': 2,
        'cat': 1,
        'nome': "marreta",
        'dano': 6,
        'hit': 60,
        'tipo': 0,
        'desc': "arma lenta e incontrolável, mas com uma força tremenda."
    },
    {
        'id': 3,
        'cat': 1,
        'nome': "lança antiga",
        'dano': 5,
        'hit': 95,
        'tipo': 2,
        'desc': "uma velha lança, confiavel apesar de ter perdido seu fio"
    },
    {
        'id': 4,
        'cat': 1,
        'nome': "mão morta",
        'dano': 2,
        'hit': 85,
        'tipo': 7,
        'desc': "mão decepada de um ser sobrenatural, emana morte"
    }       
]

listaArmaduras = [
    {
        'id': 0,
        'cat': 2,
        'nome': "camisa",
        'res': [0,0,0,0,0,0,1,0],
        'desc': "roupa simples de pano mediocre"
    },
    {
        'id': 1,
        'cat': 2,
        'nome': "armadura enferujada",
        'res': [1,3,1,-2,-5,0,-2,0],
        'desc': "uma armadura chegando a seu limite,"
    },
    {
        'id': 2,
        'cat': 2,
        'nome': "traje de medico",
        'res': [1,1,1,-2,0,10,2,5],
        'desc': "trage de couro, abafado e apertado, possui uma mascara similar a face de um passaro"
    },
    {
        'id': 3,
        'cat': 2,
        'nome': "trapo amaldiçoado",
        'res': [0,-2,-2,-1,2,0,-5,15],
        'desc': "mal pode ser considerado uma roupa, forças sobrenaturais os habitam"
    }, 
    {
        'id': 4,
        'cat': 2,
        'nome': "armadura decorativa",
        'res': [1,1,1,-3,-5,0,-1,0],
        'desc': "muito bonita mas não util"
    }   
]

# classes para itens


class Item:

    #adicionar contador de id que reseta entre runs - diferente do id da biblioteca

    contId = 0

    def __init__(self,nome:str,desc:str,cat:int):
        self.nome = nome
        self.desc = desc
        self.cat = cat
        self.id = self.contId
        self.contId += 1

    def resetarId(self):
        contId = 0


class itemUsavel(Item):

    def __init__(self, nome, desc, cat,usavel:bool,tipo:int,tipoDano:int|None,add:int|None,alvo:int,valor:int,valorAdd:int):
        super().__init__(nome, desc, cat)
        self.usavel = usavel
        self.tipo = tipo
        self.tipoDano = tipoDano
        self.add = add
        self.alvo = alvo
        self.valor = valor
        self.valorAdd = valorAdd

    def usarItem(self, alvo):
        if not self.usavel:
            print("item não é usavel")
            return

        match self.tipo:
            case 0:
                self.__danificar(alvo)
            case 1:
                self.__curar(alvo)
            case 2:
                print("nao implementado")
            case 3:
                print("Nao implementado")
        if self.add:
            match self.add:
                case 0:
                    self.__danificar(alvo)
                case 1:
                    self.__curar(alvo)
                case 2:
                    print("nao implementado")
                case 3:
                    print("Nao implementado")


    def __danificar(self, alvo):
        if hasattr(alvo, "levarDanoRes") and callable(alvo.levarDanoRes):
            alvo.levarDanoRes(self.valor, self.tipoDano)
            return
        else:
            if hasattr(alvo, "levarDano") and callable(alvo.levarDano):
                alvo.levarDano(self.valor)
                return
        return

    def __curar(self, alvo):
        alvo.curar(self.valor)



class itemArma(Item):

    def __init__(self, nome, desc, cat,dano:int,hit:int,tipo:int):
        super().__init__(nome, desc, cat)
        self.dano = dano
        self.hit = hit
        self.tipo = tipo

class itemArmadura(Item):

    def __init__(self, nome, desc, cat,res:list):
        super().__init__(nome, desc, cat)
        self.res = res

