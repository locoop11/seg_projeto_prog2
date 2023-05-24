from Candidate import *

class FilesHandler:
    def writeOutputList(outputList, outputFile):

        #with open(outputFile, 'w') as file:
            for i in outputList :
                
                exemplar = i[0]
                finalExemplar = str(exemplar.getName()) + ' : ' + str(exemplar.getListWords())
               
                cluster = i[1]
                finalCluster = []
                for member in cluster.members() :
                    clusterMember = str(member.getName()) + ' : ' + str(member.getListWords())
                    finalCluster.append(clusterMember)
                finalCluster.remove(finalExemplar)
                
                
                print(finalExemplar)
                print(finalCluster)
            with outputFile as file :
                file.write("#exemplar 1:\n", )

                

            
        
                
                
                    










        # with open(inputeFileCandidates, 'w') as file:
        # for i, exemplar in enumerate(listExamples):
        #     file.write("#exemplar {}:\n".format(i+1))
        #     file.write("{};{}\n".format(exemplar.getName(), ";".join(exemplar.getListWords())))
        #     file.write("#cluster {}:\n".format(i+1))
        # for member in clusters[i].members():
        #     file.write("{};{}\n".format(member.getName(), ";".join(member.getListWords())))
        #     file.write("\n")
        #     f.writelines()
        #     f.close()
        # return


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
