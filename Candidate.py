# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:13:31 2023

@author: dsant
"""
from Example import *

class Candidate(Example):
    def __init__(self, name, features, listWords):
        super().__init__(name, features)
        self._listWords = listWords
    
    def getListWords(self):
        return self._listWords
        
        