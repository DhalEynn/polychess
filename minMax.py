# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:42:25 2018

@author: nadia
"""

from numpy import inf
import chess


def tourMax(board,profondeur,boolean):
    if (profondeur==0):
        b=board.fen()
        return [utility(b,boolean),0]
    profondeur = profondeur-1
    u=-inf
    coup=None
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.copy()
        copyOfBoard.push(l)
        utiliteTour=tourMin(copyOfBoard,profondeur,boolean)[0]
        if utiliteTour>u :
            coup=l
            u=utiliteTour
    return [u,coup]


#==========================================================================================================

    
def tourMin(board,profondeur,boolean):
    if (profondeur==0):
        b=board.fen()
        return [utility(b,boolean),0]
    profondeur=profondeur-1
    coup=None
    u=-inf
    listeCoupsPossible=board.legal_moves
    for l in listeCoupsPossible:
        copyOfBoard=board.copy()
        copyOfBoard.push(l)
        utiliteTour=tourMax(copyOfBoard,profondeur,boolean)[0]
        if utiliteTour<u :
            coup=l
            u=utiliteTour
    return [u,coup]

#==========================================================================================================

def MinMax(board,profondeur,boolean):
    return tourMax(board, profondeur,boolean)   


#===========================================================================================================   

def utility(liste,boolean):
    sumNoir=0
    sumBlanc=0
    i=0
    while liste[i]!=' ':
        if liste [i]=='p':
            sumNoir+=1
            i+=1
        elif liste[i]=='n' or liste[i]=='b' or liste[i]=='r' :
            sumNoir+=3
            i+=1
        elif liste [i]=='q':
            sumNoir+=9
            i+=1
        elif liste [i]=='P':
            sumBlanc+=1
            i+=1
        elif liste[i]=='N' or liste[i]=='B' or liste[i]=='R' :
            sumBlanc+=3
            i+=1
        elif liste [i]=='Q':
            sumBlanc+=9
            i+=1
        else:
            i+=1
    if boolean == True :
        return sumBlanc-sumNoir
    return sumNoir-sumBlanc
 
    
#===================================================================================================
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
    
    