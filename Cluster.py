# 2022-2023 Programacao 2 LTI
# Grupo 027
# 54961 Daniela Rodrigues
# 60253 Hugo Silva

from Example import Example 

class Cluster(object):

    def __init__(self, examples):
        """
        Constructor for the Cluster class.
        Args:
            examples (list): A non-empty list of Examples.
        Note:
            Assumes examples is a non-empty list of Examples.
        """
        self.examples = examples
        self.centroid = self.computeCentroid()
    
   
    def update(self, examples):
        """
        Update the cluster with a new list of examples.
        Args:
            examples (list): A non-empty list of Examples.
        Returns:
            float: The amount the centroid has changed.
        Note:
            Assumes examples is a non-empty list of Examples.
            Replaces the examples with the new list and returns the amount the centroid has changed.
        """
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    
    def computeCentroid(self):
        """
        Compute the centroid of the cluster.
        Returns:
            Example: The centroid Example.
        Note:
            Computes the centroid by summing up the features of all examples and dividing by the number of examples.
        """
        vals = [0.0] * self.examples[0].dimensionality()
        for e in self.examples:
            vals = [vals[i] + e.getFeatures()[i] for i in range(len(vals))]
        centroid = Example('centroid', [v/len(self.examples) for v in vals])
        return centroid
    
    def getCentroid(self):
        """
        Get the centroid of the cluster.
        Returns:
            Example: The centroid Example.
        """
        return self.centroid
    
    def variability(self):
        """
        Compute the variability of the cluster.
        Returns:
            float: The total distance squared from each example to the centroid.
        Note:
            Computes the total distance squared from each example in the cluster to the centroid.
        """
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
    
    def members(self):
        """
        Generate the members of the cluster.
        Yields:
            Example: An example belonging to the cluster.
        Note:
            Generates each example belonging to the cluster.
        """
        for e in self.examples:
            yield e
   

    def __str__(self):
        """
        Get a string representation of the cluster.
        Returns:
            str: A string representation of the cluster.
        Note:
            Returns a string representation containing the centroid features and the names of the examples in the cluster.
        """
        names = [e.getName() for e in self.examples]
        names.sort()
        result = 'Cluster with centroid ' + str(self.centroid.getFeatures()) + ' contains:\n '
        for e in names:
            result = result + e + ', '
        return result[:-2]