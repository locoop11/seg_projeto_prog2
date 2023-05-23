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
    
    
    for line in lista[1:]:
        listWords = line.strip("\n").split("; ")
        
        dictTitles[listWords[1]] = int(listWords[0])
        dictTitles[listWords[2]] = int(listWords[0])
    
    return dictTitles
    
#Read Candidates File
def readCandidatesFile(inputFileCandidates, dictTitles):
    
    f = open(inputFileCandidates, "r")
    listC = f.readlines()
    candidatesFileLine = listC[3:]
    f.close()
    
    listCandidates = []
    listExemplars=[]
    
    stopCandidates = "#Exemplars:"
    stopExemplars = "void"
    
    
    for line in candidatesFileLine: 
        if line.strip() == stopCandidates:
            break
        else: 
            candidateRawData = line.replace("/n", "").split(";").strip()
            candidateWords = candidateRawData[1:]
            
            candidateVectorFeatures = []
            for word in candidateWords:
                feature = int(dictTitles[word])
                candidateVectorFeatures.append(feature)
                        
            candidate = Candidate(candidateRawData[0], candidateVectorFeatures, candidateWords)
            listCandidates.append(candidate)
    
    for line in candidatesFileLine :
        if line.strip() == stopExemplars:
            break
        else:
            exemplarRawData = line.replace("/n", "").split(";").strip()
            exemplarWords = exemplarRawData[1:]
            
            exemplarVectorFeatures = []
            for word in exemplarWords:
                feature = int(dictTitles[word])
                exemplarVectorFeatures.append(feature)
                        
            exemplar = Candidate(exemplarRawData[0], exemplarVectorFeatures, exemplarWords)
            listExemplars.append(exemplar)
            
    return (listCandidates, listExemplars)

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