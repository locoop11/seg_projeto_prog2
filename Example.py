# 2022-2023 Programacao 2 LTI
# Grupo 027
# 54961 Daniela Rodrigues
# 60253 Hugo Silva

class Example(object):

    """
    Example Class

    Represents an example with a name, a list of features, and an optional label.

    Args:
        name (str): The name of the example.
        features (list): The list of features of the example.
        label (optional): The label associated with the example.

    Attributes:
        name (str): The name of the example.
        features (list): The list of features of the example.
        label: The label associated with the example.

    Methods:
        dimensionality(): Returns the dimensionality of the example.
        getFeatures(): Returns a copy of the list of features.
        getLabel(): Returns the label of the example.
        getName(): Returns the name of the example.
        distance(other): Computes the distance between this example and another example.
        __str__(): Returns a string representation of the example.

    Static Methods:
        minkowskiDist(v1, v2, p): Computes the Minkowski distance of order p between two equal-length arrays.

    Note:
        The features are assumed to be an array of floats.
    """
    
    def __init__(self, name, features, label = None):
        #Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label
    
    
    def dimensionality(self):
        """
        Returns the dimensionality of the example.

        Returns:
            int: The dimensionality of the example.
        """
        return len(self.features)
    
    def getFeatures(self):
        """
        Returns a copy of the list of features.

        Returns:
            list: A copy of the list of features.
        """
        return self.features[:]
    
    def getLabel(self):
        """
        Returns the label of the example.

        Returns:
            object: The label of the example.
        """
        return self.label
    
    def getName(self):
        """
        Returns the name of the example.

        Returns:
            str: The name of the example.
        """
        return self.name
    
    def minkowskiDist(v1, v2, p):
        """
        Computes the Minkowski distance of order p between two equal-length arrays.

        Args:
            v1 (list): The first array of numbers.
            v2 (list): The second array of numbers.
            p (int): The order of the Minkowski distance.

        Returns:
            float: The Minkowski distance between v1 and v2.
        """
        """Assumes v1 and v2 are equal-length arrays of numbers
        Returns Minkowski distance of order p between v1 and v2"""
        dist = 0.0
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i])**p
        return dist**(1/p)

    def distance(self, other):
        """
        Computes the distance between this example and another example.

        Args:
            other (Example): The other example to compute the distance to.

        Returns:
            float: The distance between this example and the other example.
        """
        return Example.minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        """
        Returns a string representation of the example.

        Returns:
            str: The string representation of the example.
        """
        return self.name + ':' + str(self.features) + ':' + str(self.label)
