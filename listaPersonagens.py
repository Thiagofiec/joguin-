#inimigos 

#ia: 
# 0 = aleatoria
# 1 = agressivo, sempre faz o ataque que deixa um inimigo com menos vida 

listaInimigos = [
    {
        "id": 0,
        "nome": "espectro",
        "vida": 30,
        "resis": [5,5,5,0,0,100,0,999],
        "forca": 3,
        "agili": 5,
        "sabed": 8,
        "habilidades": [6,7], #id das habilidades
        "drops": [{0,4},{2,4}], #cat e id
        "ia": 1
    },
    {
        "id": 1,
        "nome": "golem",
        "vida": 100,
        "resis": [2,5,5,-5,-5,0,-5,0],
        "forca": 6,
        "agili": 1,
        "sabed": 1,
        "habilidades": [0,5], #id das habilidades
        "drops": [{0,4},{2,4}],
        "ia": 0
    }
]