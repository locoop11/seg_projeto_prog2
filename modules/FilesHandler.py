from modules.Candidate import *

class FilesHandler:
    def writeOutputList(outputList, outputFile):
        return


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
