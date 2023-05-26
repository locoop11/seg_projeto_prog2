# 2022-2023 Programacao 2 LTI
# Grupo 027
# 54961 Daniela Rodrigues
# 60253 Hugo Silva

import os
import sys
from Example import *
from kmeans import * 
from FilesHandler import *
 
"""
Clustering Realities Script

This script performs clustering on a set of candidates using the k-means algorithm.

Authors:
    dsant
    hsilva

Usage:
    python clusteringRealities.py <k> <titles_file> <candidates_file>

Arguments:
    k (int): Number of clusters to create.
    titles_file (str): Path to the file containing titles.
    candidates_file (str): Path to the file containing candidates.

Example:
    python clusteringRealities.py 3 titles.txt candidates.txt

Note:
    The script expects three command-line arguments: k (number of clusters), titles_file, and candidates_file.
    It reads the titles and candidates from the provided files, performs clustering using the k-means algorithm,
    and writes the output to a file named "output.txt" in the current working directory.
"""
            
def main():
    if len(sys.argv) < 4:
        print("Error: The number of arguments is not valid")
        print("Usage: python clusteringRealities.py <k> <titles_file> <candidates_file>")
        exit(-1)
    if not sys.argv[1].isdigit():
        print("Error: The number of clusters must be an integer.")
        print("Usage: python clusteringRealities.py <k> <titles_file> <candidates_file>")
        exit(-1)

    if sys.argv[2].find("titles.txt") <= 0:
        print("Error: The file name must be 'titles.txt'")
        print("Usage: python clusteringRealities.py <k> <titles_file> <candidates_file>")
        exit(-1)
    if not sys.argv[3].endswith(".txt"):
        print("Error: The file must have a .txt extension")
        exit(-1)
        
    fileT = sys.argv[2]
    fileC = sys.argv[3]
        
    #check if one of the two files is empty
    if os.path.getsize(fileT) == 0:
        print("Error: The file of titles is empty")
        exit(-1)
    elif os.path.getsize(fileC) == 0:
        print("Error: The file of candidates is empty")
        exit(-1)


    
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
    
    FilesHandler.writeOutputList(outputList, "candidates.txt")
    
    
if __name__ == '__main__':
    main()
    
