# cat = categoria, 0 = item, 1 = arma, 2 = armadura para diferenciar dentro do inventario do personagem

listaItens = [
    {
        'id': 0,
        'cat': 0,
        'nome': "poção de cura menor",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'valor': 20,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 0,
        'cat': 0,
        'nome': "poção de cura menor",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'valor': 20,
        'desc': "pequena frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 1,
        'cat': 0,
        'nome': "poção de cura",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'valor': 50,
        'desc': "frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 2,
        'cat': 0,
        'nome': "poção de cura maior",
        'usavel': True,
        'tipo': 1,
        'add': None,
        'valor': 100,
        'desc': "grande frasco de liquido vermelho, restaura vitalidade"
    },
{
        'id': 3,
        'cat': 0,
        'nome': "chave antiga",
        'usavel': False,
        'tipo': 4,
        'add': None,
        'valor': None,
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
        "res0": 0,
        "res1": 0,
        "res2": 0,
        "res3": 0,
        "res4": 0,
        "res5": 0,
        "res6": 1,
        "res7": 0,
        'desc': "roupa simples de pano mediocre"
    },
{
        'id': 1,
        'cat': 2,
        'nome': "armadura enferujada",
        "res0": 1,
        "res1": 3,
        "res2": 1,
        "res3": -2,
        "res4": -5,
        "res5": 0,
        "res6": -2,
        "res7": 0,
        'desc': "uma armadura chegando a seu limite,"
    }
]
