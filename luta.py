import random
from personagens import Heroi
from personagens import inimigo
from personagens import aliado

def batalha(heroi, aliados:list, inimigos:list):
    while inimigos:
        todos = [heroi] + aliados + inimigos
        iniciativa = rolarIniciativa(todos)

        print(iniciativa)
        break 

def rolarIniciativa(todos:list):
    ordem = []

    for membro in todos:
        valor_ini = membro.agili + random.randint(0, 5)
        ordem.append([membro, valor_ini])

    ordem.sort(key=lambda x: x[1], reverse=True)
    return ordem

def turnoInimigo(perso,todos):
    match perso.ia:
        case 0:
            #ataca alvo aleatorio
            alvos = todos(filter(isAliado))

            alvo = random.randint(0, len(alvos) -1)

            alvos[alvo].levarDanoRes
        case 1:
            #ataca alvo que vai ficar com a menor vida 

            alvos = todos(filter(isAliado))

            for i,alvo in enumerate(alvos):
                

    

def turnoJogador():
    pass

def escolherTurno(perso,todos):
    if isinstance(perso, Heroi):
        turnoJogador()
    elif isinstance(perso, inimigo):
        turnoInimigo(perso,todos)

def isInimigo(ini):
    return isinstance(ini, inimigo)

def isAliado(ali):
    return isinstance(ali, Heroi) or isinstance(ali,aliado)


      
            

