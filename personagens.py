from habilidades import listaHabilidades
from itens import listaItens
from itens import listaArmas
from itens import listaArmaduras

class personagemBase:
    vidaMax = int
    vida = int
    resis = int
    forca = int
    agili = int
    sabed = int


    def levarDano(self, quant):
        self.vida -= quant
        if self.vida <= 0:
            return False #morto
        return True #vivo



class Heroi(personagemBase):

    def __init__(self,nome, presente, habilidade):
        self.nome = nome
        self.vidaMax = 100
        self.forca = 3
        self.resis = 3
        self.agili = 3
        self.sabed = 3
        self.habilidades = []
        self.inventario = []
        self.arma = listaArmas[0]
        self.inventario.append(listaArmas[0])
        self.armadura = listaArmaduras[0]
        self.inventario.append(listaArmaduras[0])

        match presente:
            case 1:
                self.forca += 6
            case 2:
                self.vidaMax += 30
                self.resis += 3
            case 3:
                self.sabed += 10
            case 4:
                self.forca += 2
                self.vidaMax += 10
                self.resis += 1
                self.sabed += 3

        match habilidade:
            case 1:
                self.habilidades.append(listaHabilidades[0])
            case 2:
                self.habilidades.append(listaHabilidades[1])

        self.vida = self.vidaMax

    def mostrarPersonagem(self):
        print(f'nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidaMax}\n'
              f'arma: {self.arma['nome']}\n'
              f'habilidades:')
        for habilidade in self.habilidades:
            print(f'>{habilidade}')
        print('inventario:')
        for item in self.inventario:
            print(f'>{item['nome']}')



    def adiquirirItem(self, cat, id):
        match cat:
            case 0:
                for item in listaItens:
                    if id == item["id"]:
                        self.inventario.append(item)
            case 1:
                for arma in listaArmas:
                    if id == arma["id"]:
                        self.inventario.append(arma)
            case 2:
                for armadura in listaArmaduras:
                    if id == armadura["id"]:
                        self.inventario.append(armadura)

    def menuItem(self):
        while True:
            for i, item in enumerate(self.inventario):
                if i + 1 == len(self.inventario):
                    print(f'{i + 1}-{item["nome"]}')
                elif (i + 1) % 3 == 0:
                    print(f'{i + 1}-{item["nome"]}')
                else:
                    print(f'{i + 1}-{item["nome"]}', end=" | " )

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
                    print(item['nome'])
                    print(item['desc'])

                    match item['cat']:
                        case 0:
                            if item['usavel'] == True:
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
                                        print(f'{item["nome"]} usado')
                                        self.inventario.pop(itemPos -1)
                                    case 2:
                                        print(f'{item["nome"]} descartado')
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
                                        print(f'{item["nome"]} descartado')
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
                                        print(f'{item["nome"]} desiquipado')
                                        self.arma = "desarmado"
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
                                        print(f'{item["nome"]} equipado')
                                        self.arma = item
                                    case 2:
                                        print(f'{item["nome"]} descartado')
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
                                        print(f'{item["nome"]} desiquipado')
                                        self.armadura = "desarmado"
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
                                        print(f'{item["nome"]} equipado')
                                        self.armadura = item
                                    case 2:
                                        print(f'{item["nome"]} descartado')
                                        self.inventario.remove(itemPos - 1)
                                    case 3:
                                        break






