import random

def batalha(heroi, aliados:list, inimigos:list):
    while inimigos:
        todos = [heroi] + aliados + inimigos
        iniciativa = []

        for membro in todos:
            valor_ini = membro.agili + random.randint(0, 5)
            iniciativa.append([membro, valor_ini])

        iniciativa.sort(key=lambda x: x[1], reverse=True)
        
        print(iniciativa)
        break 

      
            

