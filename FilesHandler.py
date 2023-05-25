from Candidate import *

class FilesHandler:
    def writeOutputList(outputList, outputFile):

        #clusterMember e finalExemplar are two perfect form str to output
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
            print(finalExemplarsClusters)

            #with outputFile as file :
            for e in range(len(finalExemplarsClusters)):
                print("#exemplar", e+1 ,":\n", finalExemplarsClusters[e][0])
                print("#cluster", e+1  ,":\n", finalExemplarsClusters[e][1])
                     #file.write("#exemplar", e+1 ,":\n", finalExemplarsClusters[e][0])
                     #file.write("#cluster", e+1, ":\n", finalExemplarsClusters[e][1])


            #     print(finalExemplar)
            #     print(clusterMembers)

                    


            
            

             

            
        
                
                
                    










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
