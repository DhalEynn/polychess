# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:25:51 2018

@author: colliaur
"""
class board:
        def __init__(self):
            self.board="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            
        
        ## return a list of valid Move
        def validMove(self):
            nbcolonne=0
            nbligne=0
            nomcolonne=["a","b","c","d","e","f","g","h"]
            nomligne=["8","7","6","5","4","3","2","1"]
            pieceblanche=["P","R","N","B","Q","K"]
            piecenoire=["p","r","n","b","q","k"]
            liste_move=[]
            taille=len(self.board)
            i=0
            while():
                test=self.board[i]
                if (test==" "):
                    break
                elif (test=="/"):
                    nbligne=nbligne+1
                    nbcolonne=0
                elif (type(test)==int):
                    nbcolonne=nbcolonne+test
                elif(playwhite(self)==(test==test.upper())):
                    départ=nomcolonne[nbcolonne]+nomligne[nbligne]
                    liste_move="a"
                i=i+1
            return(liste_move)
                    
                    
            return(liste_move)
        def Movetour(nbligne,nbcolonne):
            return()    
        def playwhite(self):
            i=0
            while(self.board[i]!=" "):
                i=i+1
            return(self.board[i+1]=="w")