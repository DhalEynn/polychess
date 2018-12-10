##python-chess import
#https://github.com/niklasf/python-chess
import chess

def finDuGame (board):
    #do we have a winner?
    if (board.is_game_over() or board.is_stalemate() or board.is_insufficient_material()):
        print("The game is over")
        print(board.result())
        return True
    elif (board.is_fivefold_repetition() or board.is_seventyfive_moves()):
        print("The game is over because 5 repetitions or 75 moves without capture")
        print(board.result())
        return True
    else:
        return False

## Quel mouvement le joueur veut-il faire ?
# Tant que le mouvement demandé par l'utilisateur n'est pas possible,
# on redemande à l'utilisateur quel sera son mouvement.

def mouvementDemande ():
    while ("Le mouvement est impossible ou non légal"):
        mouv = input("Quel mouvement voulez vous faire : ")
        possibleMoves = board.legal_moves
        if (mouv in possibleMoves):
            return mouv
        else:
            print("Le mouvement est impossible ou non légal")

#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()

#print the board on the console
print(board)

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

    finDuGame(board)
