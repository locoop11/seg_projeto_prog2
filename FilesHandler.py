# 2022-2023 Programacao 2 LTI
# Grupo 027
# 54961 Daniela Rodrigues
# 60253 Hugo Silva

from Candidate import *
from kmeans import *

class FilesHandler:
    """
    FilesHandler Class

    Handles file operations for clustering realities.

    Methods:
        writeOutputList(outputList, outputFile): Writes the output list to a file.
        readTitlesFile(inputFileTitles): Reads the titles file and returns a dictionary of titles.
        readCandidatesFile(inputFileCandidates, dictTitles): Reads the candidates file and returns lists of candidates and exemplars.
        performClustering(listCandidates, listExamplars): Performs clustering on the given lists of candidates and exemplars.

    Note:
        This class assumes specific file formats and structures for titles and candidates files.
    """
    
    def writeOutputList(outputList, outputFile):
        """
        Writes the output list to a file.

        Args:
            outputList (list): The output list to write.
            outputFile (str): The path to the output file.

        Returns:
            None
        """
        finalExemplarsClusters = []
        for i in outputList :    
            exemplar = i[0]
            finalExemplar = ""
            finalExemplar += exemplar.getName() 
            for title in exemplar.getListWords():
                finalExemplar += '; ' + title
            cluster = i[1]
            clusterMembers = ""
            for member in cluster.members() :
                if member.getName() != exemplar.getName():
                    clusterMembers += str(member.getName())
                    for title in member.getListWords():
                        clusterMembers += "; " + title
                    clusterMembers += "\n"
            finalExemplarsClusters.append((finalExemplar, clusterMembers))

        with open(outputFile, 'w') as file:
            #with outputFile as file :
            for e in range(len(finalExemplarsClusters)):
                lineStr = "#exemplar " + str(e+1) + ":\n" + finalExemplarsClusters[e][0]
                file.writelines(lineStr)
                nextLine = "#cluster " + str(e+1)  + ":\n" + finalExemplarsClusters[e][1]
                file.writelines(nextLine)
            file.close()


    #Read Titles File
    def readTitlesFile(inputFileTitles):
        """
        Reads the titles file and returns a dictionary of titles.

        Args:
            inputFileTitles (str): The path to the titles file.

        Returns:
            dict: A dictionary of titles with their corresponding IDs.
        """
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
        """
        Reads the candidates file and returns lists of candidates and exemplars.

        Args:
            inputFileCandidates (str): The path to the candidates file.
            dictTitles (dict): A dictionary of titles with their corresponding IDs.

        Returns:
            tuple: A tuple containing the list of candidates and the list of exemplars.
        """
        
        f = open(inputFileCandidates, "r")
        listC = f.readlines()
        candidatesFileLine = listC[3:]
        f.close()
        
        listCandidates = []
        listExemplars=[]
        
        stopCandidates = "#Exemplars:"
        stopExemplars = "void"
        
        exemplarsFlag = False
        for line in candidatesFileLine: 
            if line.strip() == stopCandidates:
                exemplarsFlag = True
                continue
            elif(exemplarsFlag == False): 
                candidateRawData = line.replace("\n", "").split("; ")
                candidateWords = candidateRawData[1:]
                
                candidateVectorFeatures = []
                for word in candidateWords:
                    feature = int(dictTitles[word])
                    candidateVectorFeatures.append(feature)
                            
                candidate = Candidate(candidateRawData[0], candidateVectorFeatures, candidateWords)
                listCandidates.append(candidate)
            elif( exemplarsFlag == True):
                if line.strip() == stopExemplars:
                    break
                exemplarRawData = line.replace("\n", "").split("; ")
                exemplarWords = exemplarRawData[1:]
                
                exemplarVectorFeatures = []
                for word in exemplarWords:
                    feature = int(dictTitles[word])
                    exemplarVectorFeatures.append(feature)
                            
                exemplar = Candidate(exemplarRawData[0], exemplarVectorFeatures, exemplarWords)
                listExemplars.append(exemplar)
                    
        return (listCandidates, listExemplars)


    def performClustering(listCandidates, listExamplars, numClusters):
        """
        Performs clustering on the given lists of candidates and exemplars.

        Args:
            listCandidates (list): The list of candidates.
            listExamplars (list): The list of exemplars.

        Returns:
            list: The output list containing tuples of exemplars and their corresponding clusters.
        """
        clusters = []
        try :            
            if len(listExamplars) == 0:
                clusters = kmeans.kmeans(listCandidates, numClusters)
            else:
                clusters = kmeans.kmeans(listCandidates, numClusters, False, listExamplars)
        except Exception as e:
            raise Exception("Cannot perform clustering with " + str(numClusters) + " clusters")

        outputList = []
        for cluster in clusters:
            minDist = 10000
            clusterMember = None
            for exampler in cluster.members():
                thisDistance = exampler.distance(cluster.getCentroid())
                if thisDistance < minDist:
                    minDist = thisDistance
                    clusterMember = exampler
            outputList.append((clusterMember, cluster))

        return outputList
