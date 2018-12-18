# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:42:25 2018

@author: nadia
"""

from numpy import inf
import chess

def tourMax(board,profondeur):
    print("hello max")
    if (profondeur==0):
        return [1,0]
    profondeur=profondeur-1
    u=-inf
    coup=None
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.root()
        copyOfBoard.push(l)
        utiliteTour=tourMin(copyOfBoard,profondeur)[0]
        if utiliteTour>u :
            coup=l
            u=utiliteTour
    return [u,coup]
    
def tourMin(board,profondeur):
    print("hello min")
    if (profondeur==0):
        return [1,0]
    profondeur-=1
    coup=None
    u=-inf
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.root()
        copyOfBoard.push(l)
        utiliteTour=tourMax(copyOfBoard,profondeur)[0]
        if utiliteTour<u :
            coup=l
            u=utiliteTour
    return [u,coup]


def MinMax(board,profondeur):
    print("hello minMax")
    return tourMax(board, profondeur)   



# parcours de liste 
    #arret au premier espace
    #si mini point au noir
    #sinon contraire
    #nombre de point en foction de la lettre 
    # p=1 N=3 B3 R=3 Q=9 K=0
    #somme des points des blanc et celui des noir 
    #booléen en entrée pour noir (0) et blanc(1)
    #si 1 blanc-noir sinon inverse
    

    #============================================================================================================
    #       ALPHA-BETA PRUNING ALGORITHM
    #   fonctions needeed : - alphaBeta(startingNode)
    #                       - tourMax(node, alpha, beta)
    #                       - tourMin(node, alpha, beta)
    #                       - transition(node)
    #                       - utilite(node)
    #
    # transition(node) retourne l'enemble des noeuds successeurs exactement un noeuds successeur par action possible
    #
    #               - alphaBeta(startingNode)
    # 1.return the move chosen by tourMax(startingNode,-infini,+infini)
    #
    #               - tourMax(node, alpha, beta)
    # 1. if node correspond to an end of game, return utilité(n)
    # 2. u=-infini and a=void
    # 3. for each (a',n') given by transition(node)
    #       if the utility of tourMin(n',alpha,beta)>u then a=a' and u= utility of tourMin(n',alpha,beta)
    #       if u>=beta return u and a 
    #       alpha=max(alpha,u)
    # 4. return u and a
    #
    #               - tourMin(node, alpha, beta)
    #    1. if node correspond to an end of game, return utilité(n)
    # 2. u=+infini and a=void
    # 3. for each (a',n') given by transition(node)
    #       if the utility of tourMax(n',alpha,beta)<u then a=a' and u= utility of tourMax(n',alpha,beta)
    #       if u<=alpha return u and a 
    #       beta=max(beta,u)
    # 4. return u and a
    #=================================================================================================
    
    