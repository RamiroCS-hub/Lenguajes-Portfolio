from random import seed
from random import randint
from os import system

class Player:
    arrCh = ["Piedra","Papel","Tijera"]
    def __init__(self,name):
        self.win = 0
        self.lose = 0
        self.ver = True
        self.name = name
    def choose(self,ch):
        self.ch = ch
        
def randomNumber():
    num = randint(0,2)
    return num

def whoWin(ply1,ply2):
    if ply1.ch > ply2.ch:
        ply1.win += 1
        return ply1.name
    elif ply1.ch < ply2.ch:
        ply1.lose += 1
        return ply2.name
    else:
        return False

def play(player1,pC):
    while player1.ver==1:
        player1.choose(int(input("[0] Piedra, [1] Papel, o [2] tijeras?")))
        pC.choose(randomNumber())
        win = whoWin(player1,pC)
        if type(win) == type(""):
            if win == player1.name:
                print("Muy bien ",player1.name,",GANASTE!")
            else:
                print("Lo siento, el PC saco ",pC.arrCh[pC.ch]," y gano:")
        else:
            print("Fue un empate!")
        print(f"\n {player1.name} de {player1.win + player1.lose} partidas llevas: {player1.win} ganadas y {player1.lose} perdidas...")
        player1.ver = bool(input("[1] para jugar de nuevo, [0] para salir"))

def init():
    seed(1)
    print("---------PREPARADO PARA JUGAR?---------\n")
    name = input("Ingrese su nombre: ")
    player1 = Player(name)
    pC = Player("PC")
    play(player1,pC)
    print("Nos vemos!")
init()


