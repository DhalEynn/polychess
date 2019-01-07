"""
@author: Team Alpha0
"""

#python-chess import
#https://github.com/niklasf/python-chess
import chess

#used to access Polyglot book
import chess.polyglot
# used to access minMax
import minMax


#set the initial position
board = chess.Board()
maxWeight=0
move=""

#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move(), entry.weight, entry.learn)
        if entry.weight>maxWeight:
            maxWeight=entry.weight
            move= entry.move()
    if move=='':
        minMax(board,3,True)
print(maxWeight)
print(move)


