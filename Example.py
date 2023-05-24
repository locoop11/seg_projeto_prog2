class Example(object):

    """Construtor da classe example. Recebe 3 parâmetros: nome do exemplo, lista de carateristicas do exemplo e a label é opcional"""
    def __init__(self, name, features, label = None):
        #Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label
    
    
    """ Retorna a dimensionalidade do exemplo, que é igual ao comprimento da lista de carateristicas"""
    def dimensionality(self):
        return len(self.features)
    
    """Retorna uma cópia lista de carateristicas do exemplo """
    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label
    
    """Retorna o nome do exemplo"""
    def getName(self):
        return self.name
    
    """calcula a distância de Minkowski de ordem p entre dois vetores v1 e v2"""
    def minkowskiDist(v1, v2, p):
        """Assumes v1 and v2 are equal-length arrays of numbers
        Returns Minkowski distance of order p between v1 and v2"""
        dist = 0.0
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i])**p
        return dist**(1/p)

    """calculo da distância euclidiana entre o exemplo atual e outro exemplo"""
    def distance(self, other):
        return Example.minkowskiDist(self.features, other.getFeatures(), 2)

        """ Retorna uma representação da string do exemplo, no formato: nomeExemplo:caraterisitcas:label(CasoExista)"""
    def __str__(self):
        return self.name + ':' + str(self.features) + ':' + str(self.label)
