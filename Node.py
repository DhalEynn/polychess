# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:40:39 2018

@author: nadia
"""
class Node:
    def __init__(self,labels,children=[]):
        self.labels=labels
        self.children=children
    def get_labels(self):
        return self.labels
    
    def get_children(self):
        return self.children
