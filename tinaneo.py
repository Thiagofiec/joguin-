from operator import truediv

# cat = categoria, 0 = item, 1 = arma, para diferenciar dentro do inventario do personagem

# para alvo, 0= voce, 1 = inimigo
# para tipo, 0= dano, 1= cura, 3= condição, 4= casos especiais
# add sao efeitos adicionais, se None nao tem se um numero igual a tipo
listaHabilidades = [
    {
        'id': 0,
        'nome': 'Golpe poderoso',
        'alvo': 1,
        'tipo': 0,
        'add': None,
        'custo': 2,
        'desc': "um podereso golpe, causando dano adicional"
    },
    {
        'id': 1,
        'nome': 'Regis',
        'alvo': 0,
        'tipo': 1,
        'add': None,
        'custo': 5,
        'desc': "uma arte magica esquecida, curando o corpo"
    }


]


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
    }
]
class Heroi:

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
                item = object
                for item in listaItens:
                    if id == item["id"]:
                        self.inventario.append(item)
            case 1:
                for arma in listaArmas:
                    if id == arma["id"]:
                        self.inventario.append(arma)



#def procurarItem(item):
 #   for i in range(0, len(inventario)):
  #      if inventario[i] == item:
   #         return True
    #    else:
     #       return False


#def vefificarEvento(evento):
 #   for i in range (0,len(eventos)):
  #      if eventos[i] == evento:
  #          return True
   #     else:
    #        return False

while True:
    nome = str(input("escolha seu nome:"))



    while True:
        try:
            presente = int(input("Escolha seu presente:\n"
                                 "1- Força para mover o mundo\n"
                                 "2- um corpo inquebravel\n"
                                 "3- a sabedoria das maiores mentes\n"
                                 "4- um pouco de tudo\n>"))
        except ValueError:
            print('Isso não é uma opção')
            print()
        else:
            if 1 <= presente <= 4:
                break
            else:
                print('Isso não é uma opção')
                print()

    while True:
        try:
            habilidade = int(input("Recorde-se de uma memoria esquecida:\n"
                                   "1- uma batalha rapida e brutal, que acabou em unico golpe\n"
                                   "2- artes misticas apagadas pela historia\n>"))
        except ValueError:
            print('Isso não é uma opção')
            print()
        else:
            if 1 <= habilidade <= 3:
                break
            else:
                print('Isso não é uma opção')
                print()

    personagem = Heroi(nome,presente,habilidade)
    print()
    personagem.mostrarPersonagem()
    print()
    personagem.adiquirirItem(0,1)
    print()
    personagem.mostrarPersonagem()

# proximo passo adicionar inventario interativo onde se consegue ver os itens, usar itens usaveis e equipar armas




