import random
from Cluster import *

class kmeans:
    
    """Recebe uma lista de exemplos, nº de clusters """
    def kmeans(examples, k, verbose = False):
         #Get k randomly chosen initial centroids, create cluster for each
         initialCentroids = random.sample(examples, k)
         clusters = []
         for e in initialCentroids:
             clusters.append(Cluster([e]))
    
     #Iterate until centroids do not change
         converged = False
         numIterations = 0
         while not converged:
             numIterations += 1
             #Create a list containing k distinct empty lists
             newClusters = []
             for i in range(k):
                 newClusters.append([])
    
     #Associate each example with closest centroid
             for e in examples:
     #Find the centroid closest to e
                 smallestDistance = e.distance(clusters[0].getCentroid())
                 index = 0
                 for i in range(1, k):
                     distance = e.distance(clusters[i].getCentroid())
                     if distance < smallestDistance:
                         smallestDistance = distance
                         index = i
                 #Add e to the list of examples for appropriate cluster
                 newClusters[index].append(e)
    
             for c in newClusters: #Avoid having empty clusters
                 if len(c) == 0:
                     raise ValueError('Empty Cluster')
        
             #Update each cluster; check if a centroid has changed
             converged = True
             for i in range(k):
                 if clusters[i].update(newClusters[i]) > 0.0:
                     converged = False
             if verbose:
                 print('Iteration #' + str(numIterations))
                 for c in clusters:
                     print(c)
                 print('') #add blank line
         return clusters
     
    def dissimilarity(clusters):
        totDist = 0.0
        for c in clusters:
            totDist += c.variability()
        return totDist
    
    def trykmeans(examples, numClusters, numTrials, verbose = False):
         """Calls kmeans numTrials times and returns the result with the
         lowest dissimilarity"""
         best = kmeans(examples, numClusters, verbose)
         minDissimilarity = dissimilarity(best)
         trial = 1
         while trial < numTrials:
             try:
                 clusters = kmeans(examples, numClusters, verbose)
             except ValueError:
                 continue #If failed, try again
             currDissimilarity = dissimilarity(clusters)
             if currDissimilarity < minDissimilarity:
                 best = clusters
                 minDissimilarity = currDissimilarity
             trial += 1
         return best