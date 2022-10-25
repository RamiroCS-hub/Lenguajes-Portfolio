class Board:
    def __init__(self):
        self.actualBoard = [["-" for i in range(3)]for i in range(3)]
        self.turn = True

    def printBoard(self):
        for row in self.actualBoard:
            for col in row:
                print(col,end=" ")
            print()

    def changeTurn(self,played):
        if played:
            self.turn = not self.turn

    def changeBoard(self,x,y):
        if self.actualBoard[x][y] == "-":
            if self.turn:
                self.actualBoard[x][y] = "X"
            else:
                self.actualBoard[x][y] = "O"
            return True
        else:
            print("NO SE PUEDE JUGAR AHI")
            return False

    def winOrNot(self):
        self.ply = ("O","X")[self.turn]
        win = None

        for row in range(len(self.actualBoard)):
            win = True
            for col in range(len(self.actualBoard)):
                if self.actualBoard[row][col] != self.ply:
                    win = False
                    break
            if win:
                return win,self.ply
        
        
        for row in range(len(self.actualBoard)):
            win = True
            for col in range(len(self.actualBoard)):
                if self.actualBoard[col][row] != self.ply:
                    win = False
                    break
            if win:
                return win,self.ply

        win = True
        for row in range(len(self.actualBoard)):
            if self.actualBoard[row][col] != self.ply:
                win = False
                break
        if win:
            return win,self.ply    

        win = True
        for row in range(len(self.actualBoard)):
            if self.actualBoard[row][2-row] != self.ply:
                win = False
                break
        if win:
            return win,self.ply

        return False,self.ply

    def fullBoard(self):
        for row in range(len(self.actualBoard)):
            for col in range(len(self.actualBoard)):
                if self.actualBoard[row][col] == "-":
                    return False
        return True

def play(board):
    while True:
        print("Es turno del jugador ",("2","1")[board.turn])
        x = int(input("Ingrese la posicion de fila: "))
        y = int(input("Ingrese la posicion de columna: "))
        turn = board.changeBoard(x,y)
        win, whoWon = board.winOrNot()
        board.changeTurn(turn)
        board.printBoard()
        fullBoard = board.fullBoard()

        if win:
            print(f"FELICIDADES {whoWon} ganó")
            break

        if fullBoard:
            print("EMPATE")
            break
        
def init():
    ver = 1
    while ver == 1:
        board = Board()
        board.printBoard()
        play(board)
        ver = int(input("[1] para jugar de nuevo,[0] para salir"))

init()