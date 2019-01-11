"""
@author: Team Alpha0
"""

##python-chess import
#https://github.com/niklasf/python-chess
import chess
from minMax import MinMax
import random
import datetime
from os import listdir, rename
from os.path import isfile, join

## Is the game ready to end ?
# Search if an ending condition has been triggered.

def finDuGame (board, listm, file):
    #do we have a winner?
    if (board.is_game_over() or board.is_stalemate() or board.is_insufficient_material() or board.is_fivefold_repetition() or board.is_seventyfive_moves()):
        print("")
        print(board)
        saving2(file, listm, board.result())
        if (board.is_fivefold_repetition() or board.is_seventyfive_moves()):
            print("")
            print(board)
            print("The game is over because 5 repetitions or 75 moves without capture")
            print(board.result())
            return False
        else:
            print("GO : ", board.is_game_over(), "\nSTA :", board.is_stalemate(), "\nINS :", board.is_insufficient_material())
            print("The game is over")
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

## Create the savefile for the game

def creagame (savefile, PLAYER):
    path = savefile[1]
    file = open(path, "w")
    file.write("[Event \"Polychess > all\"]\n")
    file.write("[Site \"Polytech Annecy\"]\n")
    today = datetime.date.today()
    sy = str(today)
    a = ""
    for k in sy:
        if (k == "-"):
            a += "."
        else:
            a += str(k)
    file.write("[Date \"" + a + "\"]\n")
    roun = input("Actual round :\n")
    file.write("[Round \""+ roun +"\"]\n")
    if (PLAYER):
        white = input("Name of the player with the whites :\n")
        file.write("[White \""+ white +"\"]\n")
    else:
        file.write("[White \"PolyBotChess\"]\n")
    file.write("[Black \"PolychessBot\"]\n")
    file.write("[Result \"*\"]\n\n")
    file.write("1.")
    file.close()
    
## Save the new moves
    
def saving(fichier, listm):
    fileLec = open(fichier[1], "r")
    lec = []
    for x in fileLec:
        lec.append(x)
    fileLec.close()
    file = open(fichier[1], "w")
    for i in range (0, 7):
        file.write(lec[i])
    file.write("\n")
    temp = ""
    for a in listm:
        temp = temp + " " + a
    temp = temp[1:]
    file.write(temp)
    file.close()

# Save a finished game

def saving2(fichier, listm, result):
    fileLec = open(fichier[1], "r")
    lec = []
    for x in fileLec:
        lec.append(x)
    fileLec.close()
    file = open(fichier[1], "w")
    for i in range (0, 6):
        file.write(lec[i])
    file.write("[Result \""+ result +"\"]\n")
    file.write("\n")
    temp = ""
    for a in listm:
        temp = temp + " " + a
    temp = temp[1:]
    file.write(temp)
    os.rename(fichier[1], "./SAVES/COMPLETED/" + fichier[0])
    file.close()

## Input a name for the gamefile
# Make sure that the name isn't already used

def teststr(liste_nom, PLAYER):
    liste_nom += [f for f in listdir("./SAVES/COMPLETED/") if (isfile(join("./SAVES/COMPLETED/", f)) and f.endswith(".pgn"))]
    test=True
    while(test):
        string=input("Name your save with only numbers and letters (2 to 16) :\n")
        if (not(len(string)>16 or len(string)<2)):
            for k in range (len(string)):
                if (ord(string[k])<48 or 57<ord(string[k])<65 or 90<ord(string[k])<96 or ord(string[k])>122):
                    test=True
                    break
                else:
                    test=False
        if (test == False):
            string = string.lower()
            if (PLAYER):
                for n in liste_nom:
                    if n == string + ".pgn":
                        test = True
                        break
            else:
                for n in liste_nom:
                    if n == "AI-" + string + ".pgn":
                        test = True
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
            while (EXISTING != str(0) and EXISTING != str(1)):
                EXISTING = str(input("Do you want to open an already saved game (1 - yes, 0 - no) ?\n"))
        else:
            EXISTING = str(0)
        # Test for opening an already saved game
        if (EXISTING == str(1)):
            EXISTING = str(-1)
            value = -1
            print ("Here are all saved games : ")
            for i in range (len(allFiles)):
                print (i, "-", allFiles[i])
            print ("\n", len(allFiles), "- Back to game menu")
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
                if (savefile[0][0] == "A" and savefile[0][1] == "I" and savefile[0][2] == "-"):
                    PLAYER = False;
                else:
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
                savefile = teststr(allFiles, PLAYER)
            else:
                savefile = teststr(allFiles, PLAYER)
                savefile = ("AI-" + savefile[0], "./SAVES/AI-" + savefile[0])
            creagame(savefile, PLAYER)
        
    temp = open(savefile[1], "r")
    for x in temp:
        if (x[0] == "1" and x[1] == "."):
            break
        else:
            print (x)
    list_moves = x.split(" ")
    i = 0
    if (len(list_moves) > 1):
        for val in list_moves:
            if (i != 0 and val != ""):
                board.push(chess.Move.from_uci(val))
            i += 1
            if (i == 3):
                i = 0
    temp.close()
        
    # ==========================================================================
    # Game gestion (saving game, playing)
    while (finDuGame(board, list_moves, savefile) and NQUIT):
        turn = list_moves[len(list_moves) - 1][0]
        print ("Turn", turn)
        # Player versus AI
        if (PLAYER == True):
            movement = mouvementDemande(board)
            list_moves.append(movement[0])
            board.push(movement[1])
            if (finDuGame(board, list_moves, savefile)):
                print("AI turn :")
                print("")
                print(board)
                coup = MinMax(board, smart, colorAI)
                list_moves.append(str(coup))
                board.push(coup)

        # AI versus AI
        else:
            print("")
            print(board)
            print("\nWhite AI turn :")
            psmov = board.legal_moves
            numero = random.randint(0, psmov.count()-1)
            i=0
            for move in psmov:
                if i==numero:
                    list_moves.append(str(move))
                    board.push(move)
                    break
                i+=1
            print(board)
            if (finDuGame(board, list_moves, savefile)):
                print("Black AI turn :")
                coup = MinMax(board, smart, 0)
                list_moves.append(str(coup))
                board.push(coup)
            
        # Saving the game + quit
        print(board, "\n")
        list_moves.append(str(int(turn) + 1) + ".")
        saving(savefile, list_moves)
        print("Game saved in", savefile[0])
        temp = input("Do you want to quit the game (y or n) ?\n")
        if (temp == "y"):
            print ("You have quitted the game. See you at another time !")
            NQUIT = False

"""
    Start Programm
"""

main()