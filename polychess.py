"""
@author: Team Alpha0
"""

##python-chess import
#https://github.com/niklasf/python-chess
import chess
from minMax import MinMax
import time
from os import listdir
from os.path import isfile, join

## Is the game ready to end ?
# Search if an ending condition has been triggered.

def finDuGame (board):
    #do we have a winner?
    if (board.is_game_over() or board.is_stalemate() or board.is_insufficient_material()):
        print("")
        print(board)
        print("The game is over")
        print(board.result())
        return False
    elif (board.is_fivefold_repetition() or board.is_seventyfive_moves()):
        print("")
        print(board)
        print("The game is over because 5 repetitions or 75 moves without capture")
        print(board.result())
        return False
    else:
        return True

## What is the move wanted by the player ?
# Until the move written by the player is impossible,
# we ask another time what move he want to do.

def mouvementDemande (board):
    print("")
    print(board)
    while ("The move isn't possible or isn't legal"):
        possibleMoves = board.legal_moves
        temp = input("What move do you want to do (do) : \n")
        mouv = chess.Move.from_uci(temp)
        if (mouv in possibleMoves):
            return (temp, mouv)
        else:
            print("The move isn't possible or isn't legal")

##
#
#

def teststr(liste_nom):
    liste_nom += [f for f in listdir("./SAVES/COMPLETED/") if (isfile(join("./SAVES/COMPLETED/", f)) and f.endswith(".pgn"))]
    test=True
    while(test):
        string=input("name for save with only Number and letters")
        if (not(len(string)>16 or len(string)<2)):
            for k in range (len(string)):
                if (ord(string[k])<48 or 57<ord(string[k])<65 or 90<ord(string[k])<96 or ord(string[k])>122):
                    test=True
                    break
                else:
                    test=False
        if (test == False):
            for n in liste_nom:
                if n == string + ".pgn":
                    test=True
                    break
    return (string + ".pgn", "./SAVES/" + string + ".pgn")

## Main function for the program.
# The backbone of the program, with the gestion of the game.
# Features loading/saving gestion, play modes and the game.

def main ():
    #set the board to its initial position
    #corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    board = chess.Board()
    #initialiser
    movement = [0, 0]
    list_moves = []
    NQUIT = True
    smart = 2
    colorAI = 0
    # ==========================================================================
    # Main menu (loading saved games, creating new games)
    EXISTING = str(-1)
    NOTRETOUR = True
    while (NOTRETOUR):
        # Make a list of all the .pgn files in the SAVES folder
        allFiles = [f for f in listdir("./SAVES/") if (isfile(join("./SAVES/", f)) and f.endswith(".pgn"))]
        if (len(allFiles) != 0):
            print ("Here are all saved games : ")
            for i in range (len(allFiles)):
                print (i, "-", allFiles[i])
            while (EXISTING != str(0) and EXISTING != str(1)):
                EXISTING = str(input("Do you want to open an already saved game (1 - yes, 0 - no) ?\n"))
        else:
            EXISTING = str(0)
        # Test for opening an already saved game
        if (EXISTING == str(1)):
            EXISTING = str(-1)
            value = -1
            print ("\n", len(allFiles), "- Retour")
            while (value < 0 or value > len(allFiles)):
                value = str(input("What file do you want to load : \n"))
                try:
                    value = int(value)
                except:
                    print("Enter a valid number : between 0 and", len(allFiles))
            if (value == len(allFiles)):
                print ("Return to main menu")
            else:
                # ==========================================================================
                tempfile = allFiles[value]
                savefile = (tempfile, "./SAVES/" + tempfile)
                PLAYER = True;
                # ==========================================================================
                NOTRETOUR = False
        else:
            print ("New Game :")
            NOTRETOUR = False
            # Check how the player want to play :
            # Player vs Computer or Computer vs Computer
            PLAYER = False;
            jeu = input ("Do you want to play against AI (1) or see an AI play against another AI (2) ?\n")
            if (int(jeu) < 2):
                PLAYER = True
            savefile = teststr(allFiles)
    # ==========================================================================
    # Game gestion (saving game, playing)
    while (finDuGame(board) and NQUIT):
        # Player versus AI
        if (PLAYER == True):
            movement = mouvementDemande(board)
            board.push(movement[1])
            print("AI turn :")
            print("")
            print(board)
            coup = MinMax(board, smart, colorAI)
            board.push(coup)

        # AI versus AI
        else:
            print("")
            print(board)
            print("White AI turn :")
            coup = MinMax(board, smart, 1)
            board.push(coup)
            print("")
            print(board)
            print("Black AI turn :")
            coup = MinMax(board, smart, 0)
            board.push(coup)
        # Saving the game + quit
        print(board, "\n")
        print("Game saved in ", savefile[0], savefile[1])
        temp = input("Do you want to quit the game (y or n) ?\n")
        if (temp == "y"):
            print ("You have quitted the game. See you at another time !")
            NQUIT = False

"""
    Start Programm
"""

main()


#print the board on the console
"""print(board)

#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position
moves = board.legal_moves

#how many moves are available?
print(moves.count())

#iterate over all the moves
for move in moves:

    #display the move
    print(move)

    #save the current position
    current_board = board

    #do the move
    board.push(move)

    #display the board
    print(board)

    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))

    #undo the move
    board.pop()

    finDuGame(board)"""

"""
THE TESTS
"""
"""
#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()


a = mouvementDemande ()
print ("a : ", a)
print(a[0])
#save the current position
current_board = board
#do the move
board.push(a[1])
#display the board
print(board)

print("\nPlayer 2 :")

a = mouvementDemande ()
print ("a : ", a)
print(a[0])
#save the current position
current_board = board
#do the move
board.push(a[1])
#display the board
print(board)
"""
