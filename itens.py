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
        'add': None,
        'alvo': 1,
        'valor': 20,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 0,
        'cat': 0,
        'nome': "poção de acido menor",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'alvo': 2,
        'valor': 20,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 1,
        'cat': 0,
        'nome': "poção de cura",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'alvo': 1,
        'valor': 50,
        'valorAdd': None,
        'desc': "frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 2,
        'cat': 0,
        'nome': "poção de cura maior",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'alvo': 1,
        'valor': 100,
        'valorAdd': None,
        'desc': "grande frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 3,
        'cat': 0,
        'nome': "chave antiga",
        'usavel': False,
        'tipo': 4,
        'add': None,
        'alvo': 0,
        'valor': None,
        'valorAdd': None,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
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
    }
]

# classes para itens

class item:
    nome = str
    desc = str
    cat = int
    contId = 0

    def __init__(self,nome:str,desc:str,cat:int):
        self.nome = nome
        self.desc = desc
        self.cat = cat
        self.id = self.contId
        self.contId += 1

    def resetarId():
        contId = 0


class itemUsavel(item):

    def __init__(self, nome, desc, cat,usavel:bool,tipo:int,add:int|None,alvo:int,valor:int,valorAdd:int):
        super().__init__(nome, desc, cat)
        self.usavel = usavel
        self.tipo = tipo
        self.add = add
        self.alvo = alvo
        self.valor = valor
        self.valorAdd = valorAdd

        

class itemArma(item):

    def __init__(self, nome, desc, cat,dano:int,hit:int,tipo:int):
        super().__init__(nome, desc, cat)
        self.dano = dano
        self.hit = hit
        self = tipo

class itemArmadura(item):

    def __init__(self, nome, desc, cat,res:list):
        super().__init__(nome, desc, cat)
        self.res = res

