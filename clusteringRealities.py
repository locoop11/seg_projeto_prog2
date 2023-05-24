# -*- coding: utf-8 x-*-
"""
Created on Mon May 15 15:57:33 2023

@author: dsant and hsilva
"""

import sys
from Example import *
from kmeans import * 
from FilesHandler import *







# def writeFile(convertExamples, candidates):
#     f = open("C:/Users/dsant/Documents/PROG II/kmeans/projeto2/candidatesNOVOS.txt", "w")
#     for i in range(numberOfClusters):
#             f.write("Cluster" + str(i) + ":")
#             f.write(convertExamples)
        
        
def main():
    if len(sys.argv) < 4:
        print("Usage: python clusteringRealitiesTEST.py <k> <titles_file> <candidates_file>")
        return
    
    numberOfClusters = int(sys.argv[1])
    inputFileTitles = sys.argv[2]
    inputeFileCandidates = sys.argv[3]

# #     titles = 
# #     candidadates = 
#     dict = FilesHandler.readTitlesFile(inputFileTitles)
#     listExamples = FilesHandler.readCandidatesFile(inputFileCandidates, dictTitles)
    
#     listExamplars, dict = findExamplars(clusters)
#     if len(listExamplars == 0): 
#         cluster = trykmeans(listExamplars, k, 20, True)
#     else:
#         cluster = kmeans(listExamplars, 3, '', True)
    
#     writeFile(convertExamples, candidates)




titlesDict = FilesHandler.readTitlesFile("/Users/hugosilva/Documents/Code/seg_projeto_prog2/files/titles.txt")

(listCandidates, listExamplars) = FilesHandler.readCandidatesFile(
    "/Users/hugosilva/Documents/Code/seg_projeto_prog2/files/candidates.txt", titlesDict)
if len(listExamplars) == 0:
    clusters = kmeans.kmeans(listCandidates, 2)
else:
    clusters = kmeans.kmeans(listCandidates, 2, False, listExamplars)

outputList = []
for cluster in clusters:
    minDist = 10000
    clusterMember = None
    for exampler in cluster.members() :
        thisDistance = exampler.distance(cluster.getCentroid())
        if( thisDistance < minDist):
            minDist = thisDistance
            clusterMember = exampler
    outputList.append((clusterMember, cluster))

FilesHandler.writeOutputList(outputList, "/Users/gino/Code/Hugo/seg_projeto_prog2/output.txt")


    
            
    






# if __name__ == "__main__":
    
    # main()
    
    
def testFunction1() :
    
    cand1 = Example('exemplo1', [1, 2, 2, 0, 5, 6, 7, 1, 9, 10])
    cand2 = Example('exemplo2', [1, 2, 3, 0, 0, 6, 7, 8, 9, 9])
    cand3 = Example('exemplo3', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    cand4 = Example('exemplo4', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    cand5 = Example('exemplo5', [1, 2, 1, 4, 5, 6, 6, 8, 9, 8])

    candidates = [cand1, cand2, cand3, cand4, cand5]

    clusters = kmeans.kmeans(candidates, 3)

    for cluster in clusters:
        print(cluster)

    exit()