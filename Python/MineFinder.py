from random import randint
from copy import deepcopy
from os import system as sys
#N b

class Matrix:
   def __init__(self,row,column):
      self.row = row
      self.column = column

   def createLevel(self):
      self.arr = [["0" for x in range(self.row)] for y in range(self.column)]
      for i in range(self.row):
         aRow = randint(0,self.row - 1)
         aColumn = randint(0,self.column - 1)
         self.arr[aRow][aColumn] = "ñ"
         try:
            self.arr[aRow][aColumn + 1] = "1"
            print("x")
         except:
            print("mas no existe")
         try:
            self.arr[aRow][aColumn - 1] = "1"
            print("y")
         except:
            print("menos no existe")
         try:
            self.arr[aRow + 1][aColumn] = "1"
         except:
            print("mas y no existe")
         try:
            self.arr[aRow - 1][aColumn] = "1"
         except:
            print("menos y no existe")
         try:
            self.arr[aRow - 1][aColumn - 1] = "1"
         except:
            print("diago arri iz")
         try:
            self.arr[aRow + 1][aColumn + 1] = "1"
         except:
            print("diago down R")
         try:
            self.arr[aRow + 1][aColumn - 1] = "1"
         except:
            print("diago up L")
         try:
            self.arr[aRow - 1][aColumn + 1] = "1"
         except:
            print("diago down R")
         

class Player:
   def __init__(self,arr):
      self.playerArr = deepcopy(arr) 
      for i in range(len(self.playerArr)):
         for x in range(len(self.playerArr[i])):
            self.playerArr[i][x] = "?"
      
      # for elem in arr:
      #    print(elem)

   def playerMove(self,matrixArr):
      # sys("cls")
      for elem in self.playerArr:
         print(elem)
      
      x = int(input("Ingrese la pos de fila: ")) - 1
      y = int(input("Ingrese la pos de la columna: ")) - 1
      # print(matrixArr[x][y])

      if matrixArr[x][y] == "ñ":
         self.playerArr[x][y] = 2
         sys("cls")
         print("PERDISTE FRACA")
         return False
      else:
         print("Vacío")
         self.playerArr[x][y] = matrixArr[x][y]
         return True

def init():
   matrix = Matrix(10,10)
   matrix.createLevel()

   player = Player(matrix.arr)
   
   ver = True
   while ver:
      ver = player.playerMove(matrix.arr)

   # for elem in matrix.arr:
   #    print(elem)

init()


   
