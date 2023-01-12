print("Tic Tac Toe en Python !")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
columns = 3

leaveLoop = False
turnCounter = 0

# Fonction pour afficher le tableau de jeu
def printGameBoard():
  for i in range(rows):
    print("\n-------------")
    print("|", end="")
    for j in range(columns):
      print("", gameBoard[i][j], end=" |")
  print("\n-------------")

# Fonction pour savoir a qui est le tour
def modifyList(num, turn):
    num -= 1
    if(num == 0):
        gameBoard[0][0] = turn
    elif(num == 1):
        gameBoard[0][1] = turn
    elif(num == 2):
        gameBoard[0][2] = turn
    elif(num == 3):
        gameBoard[1][0] = turn
    elif(num == 4):
        gameBoard[1][1] = turn
    elif(num == 5):
        gameBoard[1][2] = turn
    elif(num == 6):
        gameBoard[2][0] = turn
    elif(num == 7):
        gameBoard[2][1] = turn
    elif(num == 8):
        gameBoard[2][2] = turn

# Fonction pour savoir qui est le gagnant
def checkForWinner(gameBoard):
    scorej1 = 0
    scorej2 = 0
    # Axe X
    if(gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    elif(gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    elif(gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    # Axe Y
    if(gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    elif(gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    elif(gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    # Victoire en diagonale
    if(gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O"
    elif(gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X"):
        scorej1 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 1 (X) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "X"
    elif(gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O"):
        scorej2 += 1
        scorej1str = str(scorej1)
        scorej2str = str(scorej2)
        print("Joueur 2 (O) a gagné!")
        print("ScoreBoard:")
        print("Joueur 1: " + scorej1str)
        print("Joueur 2: " + scorej2str)
        return "O" 
    else:
        return "Match nul"

def startGame():
    leaveLoop = False
    while(leaveLoop == False):
        possibleNumbers = [1,2,3,4,5,6,7,8,9]
        gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
        gameBoardvoid = [[1,2,3], [4,5,6], [7,8,9]]
        rows = 3
        columns = 3
        turnCounter = 0

        # Tour du joueur
        if(turnCounter % 2 == 0):
            printGameBoard()
            numberPicked = int(input("\n(Joueur 1 | X) Chosis un nombre [1-9]: "))
            if(numberPicked >= 1 or numberPicked <= 9):
                modifyList(numberPicked, 'X')
                possibleNumbers.remove(numberPicked)
            else:
                print("Nombre invalide, essaie encore.")
            turnCounter += 1
            printGameBoard()
        # Tour de l'ordinateur
        else:
            while(True):
                numberPicked = int(input("\n(Joueur 2 | O) Chosis un nombre [1-9]: "))
                if(numberPicked in possibleNumbers):
                    modifyList(numberPicked, 'O')
                    possibleNumbers.remove(numberPicked)
                    turnCounter += 1
                    break

        winner = checkForWinner(gameBoard)
        if(winner != "Match nul"):
            print("\nPartie terminée.")
            print("\nVoulez vous rejouer ?")
            break

while(leaveLoop == False):
  # Tour du joueur 1
  if(turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\n(Joueur 1 | X) Chosis un nombre [1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyList(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("Nombre invalide, essaie encore.")
    turnCounter += 1
    printGameBoard()
  # Tour du joueur 2
  else:
    while(True):
      numberPicked = int(input("\n(Joueur 2 | O) Chosis un nombre [1-9]: "))
      if(numberPicked in possibleNumbers):
        modifyList(numberPicked, 'O')
        possibleNumbers.remove(numberPicked)
        turnCounter += 1
        break

  winner = checkForWinner(gameBoard)
  if(winner != "Match nul"):
    print("\nPartie terminée.")
    print("\nVoulez vous rejouer ? yes/oui ou no/non")
    remake = input("")
    if remake == "yes" or "oui":
        startGame()
    else:
        quit

startGame()