# -*- coding: utf-8 x-*-
"""
Created on Mon May 15 15:57:33 2023

@author: dsant and hsilva
"""
import os
import sys
from Example import *
from kmeans import * 
from FilesHandler import *
 
            
def main():
    if len(sys.argv) < 4:
        print("Usage: python clusteringRealities.py <k> <titles_file> <candidates_file>")
        return
    
    numberOfClusters = int(sys.argv[1])        
    inputFileTitles = sys.argv[2]
    inputFileCandidates = sys.argv[3]

    processFiles(inputFileTitles, inputFileCandidates, numberOfClusters)

def processFiles(inputFileTitles, inputFileCandidates, numberOfClusters):
    # print("Processing files...")
    # print("Number of clusters: " + str(numberOfClusters))
    # print("Titles file: " + inputFileTitles)
    # print("Candidates file: " + inputFileCandidates)
    
    if( numberOfClusters < 1):
        raise Exception("k must be greater than 0")

    projectDirectory = os.getcwd()

    titlesFilePath = os.path.join(projectDirectory, inputFileTitles)
    candidatesFilePath = os.path.join(projectDirectory, inputFileCandidates)

    titlesDict = FilesHandler.readTitlesFile(titlesFilePath)
    (listCandidates, listExamplars) = FilesHandler.readCandidatesFile(candidatesFilePath, titlesDict)

    outputList = FilesHandler.performClustering(listCandidates, listExamplars, numberOfClusters)
    
    FilesHandler.writeOutputList(outputList, "output.txt")
    return outputList
    
if __name__ == '__main__':
    main()
    
