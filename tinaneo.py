from operator import truediv
import personagens
import luta








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
    print("Bem vindo ao menu de teste")
    while True:
        input()
        while True:
            try:
                opcao = int(input("Opçoes de teste:\n"
                                    "1- ver personagem\n"
                                    "2- adicionar item\n"
                                    "3- manejar inventario\n"
                                    "4- levar dano\n"
                                    "5- simular luta\n"
                                    "6- sair\n>"
                                    ))
            except ValueError:
                print('Isso não é uma opção')
                print()
            else:
                if 1 <= opcao <= 6:
                    break
                else:
                    print('Isso não é uma opção')
                    print()
        match opcao:
            case 1:
                personagem.mostrarPersonagem()
                print()
            case 2:
                while True:
                    try:
                        opcat = int(input("0-item\n"
                                        "1- arma\n"
                                        "2- armadura\n>"))
                    except ValueError:
                        print('smt')
                        print()
                    else:
                        if 0 <= opcat <= 2:
                            break
                        else:
                            print('Isso não é uma opção seu boboca')
                            print()
                opid = int(input("digite o id do seu item\n>"))

                personagem.adiquirirItem(opcat, opid)
            case 3:
                personagem.menuItem()
            case 4:
                dano = int(input("quanto dano levar\n>"))

                while True:
                    try:
                        danoTipo = int(input("0-impacto\n"
                                        "1- corte\n"
                                        "2- perfuração\n"
                                        "3- fogo\n"
                                        "4- raio\n"
                                        "5- veneno\n"
                                        "6- frio\n"
                                        "7- morte\n"
                                        "8- omnipotente\n>"))
                    except ValueError:
                        print('opcao invalida')
                        print()
                    else:
                        if 0 <= danoTipo <= 8:
                            break
                        else:
                            print('escolhe um dano de verdade seu trouxa')
                            print()

                if personagem.levarDanoHeroi(dano,danoTipo):
                    pass
                else: 
                    break
            case 5:
                numero = int(input("Quantos inimigos voce ira enfrentar?\n>"))
                inimigos = []

                while numero > 0:
                    idIni = int(input("id do inimigo \n>"))
                    newIni = personagens.inimigo(idIni)
                    inimigos.append(newIni)
                    numero -= 1

                luta.batalha(personagem,[],inimigos)
            
            case 6:
                print("tchau tchau")
                break
        
        
        

    
    # input()
    # personagem.adiquirirItem(0,1)
    # personagem.adiquirirItem(0, 0)
    # personagem.adiquirirItem(0, 2)
    # personagem.adiquirirItem(1, 2)
    # personagem.adiquirirItem(2, 1)
    # personagem.mostrarPersonagem()
    # input()
    # personagem.menuItem()


# proximo passo adicionar inventario interativo onde se consegue ver os itens, usar itens usaveis e equipar armas




