# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:25:51 2018

@author: colliaur
"""
#board.fen()
import math
class board:
        def __init__(self):
            self.board="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            
        def checkcase(case,fen):
            nbcolonne=0
            nbligne=0
            i=0
            while(fen[i]!= " " and (nbcolonne <= case[0] or nbligne <= case[1])):
                test=self.fen()[i]
                if (test=="/"):
                    nbligne=nbligne+1
                    nbcolonne=0
                elif (type(test)==int):
                    nbcolonne=nbcolonne+test
                else:
                    return([1,testPieceToWhite(test)]
                i=i+1
            return([0,0])
        def testPieceToWhite(caractere):
            if (test==test.upper()):
                return (1)
            else:
                return (0)

        ## return a list of valid Move
        def validMove(self):
            nbcolonne=0
            nbligne=0
            nomcolonne=["a","b","c","d","e","f","g","h"]
            nomligne=["8","7","6","5","4","3","2","1"]
            pieceblanche=["P","R","N","B","Q","K"]
            piecenoire=["p","r","n","b","q","k"]
            liste_move=[]
            taille=len()
            i=0
            while(i<len(self.fen())):
                test=self.fen()[i]
                if (test==" "):
                    break
                elif (test=="/"):
                    nbligne=nbligne+1
                    nbcolonne=0
                elif (type(test)==int):
                    nbcolonne=nbcolonne+test
                elif(playwhite(self)==testPieceToWhite(test)):
                    depart=nomcolonne[nbcolonne]+nomligne[nbligne]
                    arrivee
                    liste_move=liste_move+
                i=i+1
            return(liste_move)
                    
                    
            return(liste_move)
        
        def testMove(piece,depart,whiteToMove):
            if (piece.upper() == P):
                arrivee=movePawn(depart,whiteToMove)
            elif(piece.upper() == B):
                arrivee=moveDiagonal(depart, 8,whiteToMove)
            elif(piece.upper() == R):
                arrivee=moveVertical(depart,8,whiteToMove) + moveHorizontal(départ, 8,whiteToMove)
            elif(piece.upper() == K):
                arrivee= moveVertical(depart,1,whiteToMove) + moveHorizontal(départ, 1,whiteToMove) + moveDiagonal(départ, 1,whiteToMove)
            elif(piece.upper() == Q):
                arrivee = moveVertical(depart,8,whiteToMove) + moveHorizontal(départ, 8,whiteToMove) + moveDiagonal(départ, 8,whiteToMove)
            else(piece.upper() == N):
                arrivee == moveKnight()
            return(arrivée)
        
        def movePawn(depart,whiteToMove):
            i=1
            if (whiteToMove==1):
                sensToMove=1
            else:
                sensToMove=-1
            arrive=[depart[0],depart[1]+1*sensToMove]
            if (checkcase(case,fen)[0]):
                arrive=[]
            return(arrive)

        def moveDiagonal(depart,nb):
            i=1
            arrive=moveDiagonalDirection(depart,nb,1,1)+moveDiagonalDirection(depart,nb,1,-1)+moveDiagonalDirection(depart,nb,-1,1)+moveDiagonalDirection(depart,nb,-1,-1)
            return (arrive)

        def moveDiagonalDirection(depart,nb,i,j):
             while (math.abs(i)<=nb):
                arrive=arrive+[depart[0]+i, depart[1]+j]
                if (i>0)
                i=i+1
                j=j+1
            return(arrive)



                

        def whiteToMove(self):
            i=0
            while(self.board[i]!=" "):
                i=i+1
            return(self.board[i+1]=="w")