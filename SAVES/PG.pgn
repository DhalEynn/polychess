#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:56:00 2018

@author: princ
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:12:57 2018

@author: princ
"""
import chess.pgn

pgn = open("on appele le document donc on veut ouvir .pgn")
first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)

# we fill an event and one or two teams for playing

#first_game.headers["Event"]
#'IBM Man-Machine, New York USA'


# Iterate through all moves and play them on a board.
board = first_game.board()

# We add the algorithm in wich we use for playing with machine
board = chess.Board('4r3/6P1/2p2P1k/1p6/pP2p1R1/P1B5/2P2K2/3r4 b - - 0 45')

#Encoding from utf-8 format

pgn = open("data/pgn/kasparov-deep-blue-1997.pgn", encoding="utf-8-sig")




# The block for creating a heard of the game and with all details

import chess
import chess.pgn

game = chess.pgn.Game()
game.headers["Event"] = "Example"
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_variation(chess.Move.from_uci("e7e5"))
node.comment = "Comment"

print(game)
#[Event "Example"]
#[Site "?"]
#[Date "????.??.??"]
#[Round "?"]
#[White "?"]
#[Black "?"]
