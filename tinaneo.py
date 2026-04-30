from operator import truediv
import personagens








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

    personagem = personagens.Heroi(nome,presente,habilidade)
    input()
    personagem.mostrarPersonagem()
    input()
    personagem.adiquirirItem(0,1)
    personagem.adiquirirItem(0, 0)
    personagem.adiquirirItem(0, 2)
    personagem.adiquirirItem(1, 2)
    personagem.adiquirirItem(2, 1)
    personagem.mostrarPersonagem()
    input()
    personagem.menuItem()


# proximo passo adicionar inventario interativo onde se consegue ver os itens, usar itens usaveis e equipar armas




