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
            acao = perso.habilidades[random.randint(0, len(perso.habilidades) -1)]

            if acao['alvo'] == 1:

                alvos = [a for a in todos if isAliado(a) and a.vivo]

                alvo = random.randint(0, len(alvos) -1)

                danificar(perso.nome,acao['nome'], alvos[alvo],acao['valor'],acao['tipoDano'], False )
                match acao['add']:
                    case None:
                        pass
                    case 1:
                        danificar(perso.nome,acao['nome'],alvos[alvo],acao['addValor'],acao['addTipoDano'], True)
                    #colocar os outros tipos dps: cura, cond e especial
        case 1:
            #ataca alvo que vai ficar com a menor vida 

            alvos = [a for a in todos if isAliado(a) and a.vivo]

            alvo = 0 
            acao = 0 

            for iAl,al in enumerate(alvos):#descobrir que combinação de habilidade e alvo deixa um inimigo com menor vida
                for iAc,ac in enumerate(perso.habilidades):
                    if al.vida - ac['valor'] <= alvos[alvo] - perso.habilidades[acao]['valor']:
                        if al.vida - ac['valor'] == alvos[alvo] - perso.habilidades[acao]['valor']:
                            if random.randint(0,1) > 0:
                                alvo = iAl
                                acao = iAc
                        else:
                            alvo = iAl
                            acao = iAc

            acao = perso.habilidades[acao]

            danificar(perso.nome,acao['nome'], alvos[alvo],acao['valor'],acao['tipoDano'], False )
            match acao['add']:
                    case None:
                        pass
                    case 1:
                        danificar(perso.nome,acao['nome'],alvos[alvo],acao['addValor'],acao['addTipoDano'], True)




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

def danificar(perso,acao,alvo, quant, tipo, isadd:bool):
    if not isadd:
        print(f"{perso} usa {acao} contra {alvo} ")
    alvo.levarDanoRes(quant,tipo)

def curar(alvo, quant):
    alvo.curar(quant)

def aplicarCond():
    pass

def acaoEspecial():
    pass
            

