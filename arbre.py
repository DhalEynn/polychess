# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:42:25 2018

@author: nadia
"""

from Node import Node
from numpy import inf
import chess
class arbre(Node):
    def __init__(self,labels,sub_RTree=[]):
       super().__init__(labels,sub_RTree)
    # un arbre est représentée par sa racine alors la racine c'est lui meme
    def root(self):
        return self
    # Le sous-arbre est l'ensemble des enfants de cet arbre  
    def sub_tree(self):
        return self.children
    # un arbre vide est un arbre qui ne contient rien donc dont le label ne contient rien
    def is_empty(self):
       return self.get_labels==[]
    # retourne vrai si l'élément est un noeud i.e s'il n'a pas de fils
    def is_leaf(self):
        return self.get_children()==[]
    
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
    def transition(self):
        liste=self.legal_moves
        
  def tourMax(node,alpha,beta):
        if node.is_leaf():
            return utility(node)
        u=-inf
        listeCoupsPossible=transition(node)
        for i in range(len(listeCoupsPossible)):
            l=listeCoupsPossible[i]
            utiliteTour=utility(tourMin(l[1],alpha,beta))
            if utiliteTour>u :
                a=l[0]
                u=utiliteTour
            if u>=beta:
                return [u,a]
            alpha=max(alpha,u)
        return [u,a]
    
    def tourMin(node,alpha,beta):
        if node.is_leaf():
            return utility(node)
        u=inf
        listeCoupsPossible=transition(node)
        for i in range(len(listeCoupsPossible)):
            l=listeCoupsPossible[i]
            utiliteTour=utility(tourMax(l[1],alpha,beta))
            if utiliteTour<u :
                a=l[0]
                u=utiliteTour
            if u<=alpha:
                return [u,a]
            beta=min(beta,u)
        return [u,a]
    
    def alphaBetaPruning(startingNode):
        return tourMax(startingNode)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#   #parcours en profondeurs un arbre et affiche au fur et a mesure les noeuds parcourus
#    def display_depth(self):
#        if self.is_empty():
#            return
#        else:
#            f=Forest([self])
#            return f.display_depth()
#    #parcours en largeur un arbre et affiche au fur et a mesure les noeuds parcourus
#    def display_width(self):
#        if self.is_empty():
#            return
#        else:
#            f=Forest([self])
#            return f.display_width()
#        #donne le pere de node
#        #father(Node)->Node
#    def father(self,node):
#        if self.is_empty():
#            return
#        else:
#            foret=Forest([self])
#            return foret.father(node)
#    
#    def descending(self):
#        if self.is_empty():
#            return 
#        else:
#            foret=Forest([self])
#            return foret.descending()
#    
##    def ascending(self):
##        if self.is_empty():
##            return 
##        else:
##            foret=Forest([self])
##            return foret.ascending()
#        
#        

#    
#    #donne le dégré d'un arbre 
#    #retourne le max des dégrés des noeuds
#    def degree(self):
#        if self.is_empty():
#            return 
#        else :
#            foret=Forest([self])
#            return foret.degree()
#        
#    def depth(self):
#        if self.is_empty():
#            return 
#        else :
#            foret=Forest([self])
#            return foret.depth()