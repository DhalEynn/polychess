# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:42:25 2018

@author: nadia
"""

from Node import Node
from numpy import inf
import chess

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
    
  
   def tourMax(board,profondeur):
        if (profondeur=0):
            return (utility(board))
        profondeur=profondeur-1
        u=-inf
        listeCoupsPossible=board.legal_moves() #(action,noeudSuccesseur)
        for i in range(len(listeCoupsPossible)):
            l=listeCoupsPossible[i]
            utiliteTour=tourMin(fromMoveToBoard(l[i],board),profondeur)[0]
            if utiliteTour>u :
                coup=l[i]
                u=utiliteTour
        return [u,coup]
    
    def tourMin(board,profondeur):
        if (profondeur=0):
            return (utility(board))
        u=-inf
        listeCoupsPossible=board.legal_moves()
        for i in range(len(listeCoupsPossible)):
            l=listeCoupsPossible[i]
            utiliteTour=tourMax(fromMoveToBoard(l[i]),profondeur)[0]
            if utiliteTour<u :
                coup=l[i]
                u=utiliteTour
        return [u,coup]
    
    def minMax(board,profondeur):
        return tourMax(board,profodeur)
    