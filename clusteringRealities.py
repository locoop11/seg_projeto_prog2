## Read input arguments from program and validate K against the number of exemplars in the input file if any


###
## Read input file with candidates and convert each candidate to a vector like structure
## Function: readCandidatesFile
##
## Reponsilibilites:
## Returns: An array of candidates each candidate is a vector 
#           like structure in which each element is a feature and features are the converted number 
#           to the titles
#
#  Example of a return value: [Candidate1, Candidate2, Candidate3, ...]
#            Candidate1 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#            Canddate2 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
###

candidatesDict = readCandidatesFile(inputFileCandidates, inputFileTitles)


##
## Create the appropriate groups of candidates based on the number of clusters we need.
## Groups of cluster are by requirements defined in the K input argument or in the number of
## exemplars defined in the input file.
##
## Function: createGroupClusters
## Responsibilities: Create the appropriate groups of candidates based on the number of clusters we need.
## Returns: An array of groups of candidates
## Example of a return value: [Group1, Group2, Group3, ...]
##           Group1 : [Candidate1, Candidate2, Candidate3, ...]
##           Group2 : [Candidate1, Candidate2, Candidate3, ...]
##           Group3 : [Candidate1, Candidate2, Candidate3, ...]

groupsDict = createGroupClusters(candidatesVector, K)

##
## Compute the centroid of each group
## Having all the candidates assign to a cluster compute the candidate that is the centroid of the cluster
##
## Function: computeCentroid
## Responsibilities: Compute the centroid of each group
## Returns: An array of groups in which the first element of each group is its centroid
## Example of a return value: [Group1, Group2, Group3, ...]
##         Group1 : [candidate1, candidate2, candidate3, ...]


## Write the array of group centroids to the output file

