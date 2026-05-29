from habilidades import listaHabilidades
from habilidades import ListaHabMonstros
from itens import listaItens
from itens import listaArmas
from itens import listaArmaduras
from itens import itemUsavel
from itens import itemArma
from itens import itemArmadura
from listaPersonagens import listaInimigos

class personagemBase:
    nome = str
    vidaMax = int
    vida = int
    resis = list
    forca = int
    agili = int
    sabed = int
    vivo = bool 


    def levarDano(self, quant):
        if quant > 0:
            self.vida -= quant
            print(f"{self.nome} levou {quant} de dano")
        else:
            print(f'golpe incapaiz de danificar {self.nome}')
        if self.vida <= 0:
            self.vivo = False

    def curar(self,quant):
        self.vida += quant
        if self.vida > self.vidaMax:
            overheal = self.vida - self.vidaMax
            quantReal = quant - overheal
            self.vida = self.vidaMax
            print(f"{self.nome} curou {quantReal} pontos de vida")
        else:
            print(f'{self.nome} curou {quant} pontos de vida')




class Heroi(personagemBase):

    def __init__(self,nome, presente, habilidade):
        self.nome = nome
        self.vidaMax = 100
        self.forca = 3
        self.resis = 3
        self.agili = 3
        self.sabed = 3
        self.vivo = True
        self.habilidades = []
        self.resis = [0,0,0,0,0,0,0,0]
        self.inventario = []
        self.adiquirirItem(1,0)
        self.adiquirirItem(2,0)
        self.arma = self.inventario[0]
        self.armadura = self.inventario[1]        
        

        match presente:
            case 1:
                self.forca += 6
            case 2:
                self.vidaMax += 30
                self.resis[0:2] = [1,1,1]
            case 3:
                self.sabed += 10
            case 4:
                self.forca += 2
                self.vidaMax += 10
                self.sabed += 3

        match habilidade:
            case 1:
                self.habilidades.append(listaHabilidades[0])
            case 2:
                self.habilidades.append(listaHabilidades[1])

        self.vida = self.vidaMax

#teste

    def mostrarPersonagem(self):
        print(f'nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidaMax}\n'
              f'arma: {self.arma.nome}\n'
              f'armadura: {self.armadura}\n'
              f'resistencias: {self.resis}\n'
              f'habilidades:')
        for habilidade in self.habilidades:
            print(f'>{habilidade}')
        print('inventario:')
        for item in self.inventario:
            print(f'>{item.nome}')

#vida

    def levarDanoRes(self, quant, tipo):
        self.levarDano(quant -self.calcularRes(tipo))
            #adicionar print diferente dependendo da porcentagem da vida 
        if self.vivo == False:
            print("você perde sua energia e colapsa")
        
    def calcularRes(self, tipo):
        if tipo == 8:
            return 0
        
        if self.armadura is None:
            return self.resis[tipo] 
        
        return self.resis[tipo] + self.armadura.res[tipo]
    
#combate

    def calcularDano(self):
        if self.arma:
            return self.forca + self.arma.dano
        else:
            return self.forca
#inventario

    def adiquirirItem(self, cat, id):
        match cat:
            case 0:
                for novoItem in listaItens:
                    if id == novoItem["id"]:
                        addItem = itemUsavel(novoItem["nome"],novoItem["desc"],novoItem["cat"],novoItem["usavel"],novoItem["tipo"],novoItem["tipoDano"],novoItem["add"],novoItem["alvo"], novoItem["valor"],novoItem["valorAdd"] )
                        self.inventario.append(addItem)
                        return
                print("nenhum item valido com essa combinação de categoria e id")
                print("itens validos:")
                for item in listaItens:
                    print(f"id:{item['id']} - nome:{item['nome']}")
                input()
            case 1:
                for novaArma in listaArmas:
                    if id == novaArma["id"]:
                        addArma = itemArma(novaArma["nome"],novaArma["desc"],novaArma["cat"],novaArma["dano"],novaArma["hit"],novaArma["tipo"])
                        self.inventario.append(addArma)
                        return
                print("nenhum item valido com essa combinação de categoria e id")
                print("itens validos:")
                for arma in listaArmas:
                    print(f"id:{arma['id']} - nome:{arma['nome']}")
                input()
            case 2:
                for novaArmadura in listaArmaduras:
                    if id == novaArmadura["id"]:
                        addArmadura = itemArmadura(novaArmadura["nome"],novaArmadura["desc"],novaArmadura["cat"], novaArmadura["res"])
                        self.inventario.append(addArmadura)
                        return
                print("nenhum item valido com essa combinação de categoria e id")
                print("itens validos:")
                for armadura in listaArmaduras:
                    print(f"id:{armadura['id']} - nome:{armadura['nome']}")
                input()

    def menuItem(self):
        while True:
            for i, item in enumerate(self.inventario):
                if i + 1 == len(self.inventario):
                    print(f'{i + 1}-{item.nome}')
                elif (i + 1) % 3 == 0:
                    print(f'{i + 1}-{item.nome}')
                else:
                    print(f'{i + 1}-{item.nome}', end=" | " )

            print("0 - sair")


            while True:
                try:
                    itemPos = int(input("escolha um item: "))

                except ValueError:
                    print('Isso não é uma opção')
                    print()
                else:
                    if 0 <= itemPos <= self.inventario.__len__():
                        break
                    else:
                        print('Isso não é uma opção')
                        print()

            if itemPos == 0:
                break

            for i, item in enumerate(self.inventario):
                if i + 1 == itemPos:
                    print(item.nome)
                    print(item.desc)

                    match item.cat:
                        case 0:
                            if item.usavel == True & item.alvo == 1 :
                                while True:
                                    try:
                                        i = int(input("1-usar\n"
                                                      "2-descartar\n"
                                                      "3-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 3:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} usado')
                                        item.usarItem(self)
                                        self.inventario.pop(itemPos -1)
                                    case 2:
                                        print(f'{item.nome} descartado')
                                        self.inventario.pop(itemPos - 1)
                                    case 3:
                                        return
                            else:
                                while True:
                                    try:
                                        i = int(input("1-descartar\n"
                                                      "2-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 2:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} descartado')
                                        self.inventario.pop(itemPos - 1)
                                    case 2:
                                        return


                        case 1:
                            if item == self.arma:
                                while True:
                                    try:
                                        i = int(input("1-desiquipar\n"
                                                      "2-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 2:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} desiquipado')
                                        self.arma = None
                                    case 2:
                                        break

                            else:
                                while True:
                                    try:
                                        i = int(input("1-equipar\n"
                                                      "2-discartar\n"
                                                      "3-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 3:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} equipado')
                                        self.arma = item
                                    case 2:
                                        print(f'{item.nome} descartado')
                                        self.inventario.pop(itemPos - 1)
                                    case 3:
                                        break
                        case 2:
                            if item == self.armadura:
                                while True:
                                    try:
                                        i = int(input("1-desiquipar\n"
                                                      "2-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 2:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} desiquipado')
                                        self.armadura = None
                                    case 2:
                                        break

                            else:
                                while True:
                                    try:
                                        i = int(input("1-equipar\n"
                                                      "2-discartar\n"
                                                      "3-sair\n"
                                                      ">"))

                                    except ValueError:
                                        print('Isso não é uma opção')
                                        print()
                                    else:
                                        if 1 <= i <= 3:
                                            break
                                        else:
                                            print('Isso não é uma opção')
                                            print()

                                match i:
                                    case 1:
                                        print(f'{item.nome} equipado')
                                        self.armadura = item
                                    case 2:
                                        print(f'{item.nome} descartado')
                                        self.inventario.pop(itemPos - 1)
                                    case 3:
                                        break

class aliado(personagemBase):
    a= 1

class inimigo(personagemBase):

    def __init__(self,id:int):
        #adicionar ia dps se eu quiser
        for i, ini in enumerate(listaInimigos):
            if ini["id"] == id:
                self.nome = ini["nome"] 
                self.vida = self.vidaMax = ini["vida"]
                self.resis = ini["resis"]
                self.forca = ini["forca"]
                self.agili = ini["agili"]
                self.sabed = ini["sabed"]
                self.habilidades = []
                for hab in ini['habilidades']:
                    self.habilidades.append(ListaHabMonstros[hab])
                self.drops = ini["drops"]
                self.ia = ini["ia"] 
                self.vivo = True
            
        
    
    def levarDanoRes(self, quant,tipo):
        self.levarDano(quant - self.calcularRes(tipo))
        if not self.vivo:
            print(f'{self.nome} foi morto')

    def calcularRes(self, tipo):
        if tipo == 8:
            return 0
        return self.resis[tipo]
    


    
        





