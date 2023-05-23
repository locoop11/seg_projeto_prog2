# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:57:33 2023

@author: dsant
"""

import sys
from Example import *
from kmeans import * 
from Candidate import *

#Read Titles File
def readTitlesFile(inputFileTitles):
    f = open(inputFileTitles, "r")
    lista = f.readlines()
    f.close()

    dictTitles = {}
    listWords = []
    
    for line in lista[1:]:
        listWords = line.strip("\n").split("; ")
        dictTitles[listWords[1]] = int(listWords[0])
        dictTitles[listWords[2]] = int(listWords[0])
    
    return dictTitles
    
#Read Candidates File
def readCandidatesFile(inputFileCandidates, dictTitles):
    
    f = open(inputFileCandidates, "r")
    listC = f.readlines()
    listCandidates = listC[3:]
    f.close()
    
    listExamplars = []
    listTotalWords = []
    
    stopCandidates = "#Exemplars:"
    
    for line in listCandidates:
       
        if line.strip() == stopCandidates:
            break
        
        else: 
            listWordsC = line.replace(";", " ").replace("/n", " ").split();
            listTotalWords.append(listWordsC)
            
            vetorFeatures = []
            for element in listWordsC:
                for key, value in dictTitles.items():
                    
                    print(value)
                    if value == element:
                        vetorFeatures.append(key)
                        
            person = Candidate(listWordsC[0], vetorFeatures, listWords)
            listExamplars.append(person)

    return listExamplars

def findExamplars(cluster):
    convertExamplars = []
    return convertExamplars

def writeFile(convertExamples, candidates):
    f = open("C:/Users/dsant/Documents/PROG II/kmeans/projeto2/candidatesNOVOS.txt", "w")
    for i in range(numberOfClusters):
            f.write("Cluster" + str(i) + ":")
            f.write(convertExamples)
        
        
def main():
    if len(sys.argv) < 4:
        print("Usage: python clusteringRealitiesTEST.py <k> <titles_file> <candidates_file>")
        return
    
    numberOfClusters = int(sys.argv[1])
    inputFileTitles = sys.argv[2]
    inputeFileCandidates = sys.argv[3]

#     titles = 
#     candidadates = 
    dict = readTitlesFile(inputFileTitles)
    listExamples = readCandidatesFile(inputFileCandidates, dictTitles)
    
    listExamplars, dict = findExamplars(clusters)
    if len(listExamplars == 0): 
        cluster = trykmeans(listExamplars, k, 20, True)
    else:
        cluster = kmeans(listExamplars, 3, '', True)
    
    writeFile(convertExamples, candidates)



# a = readTitlesFile("C:/Users/dsant/Documents/PROG II/kmeans/projeto2/titles.txt")

# b = readCandidatesFile("C:/Users/dsant/Documents/PROG II/kmeans/projeto2/candidates.txt", a)

# if __name__ == "__main__":
    
    # main()