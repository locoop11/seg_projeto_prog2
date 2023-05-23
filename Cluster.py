# -*- coding: utf-8 -*-
from Example import * 

class Cluster(object):

    """Construtor da classe, recebe uma lista de exemplos(guarda os exemplos do cluster) e centroid (representa o centroide do cluster chamando o metodos computeCentroid())"""
    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.computeCentroid()
    
    """Recebe uma nova lista de exemplos como argumento.
    Substitui os elementos anteriores pelos novos e recalcula o centroide
    retorna a distância entre o antigo centroide e o novo"""
    def update(self, examples):
        """Assume examples is a non-empty list of Examples
        Replace examples; return amount centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    
    """Calcula o centroide do cluster. Inicializa uma lista 'vals' com zeros, 
    com tamanho igual ao comprimento das carateristicas do primeiro exemplo.
    Depois itera sobre os exemplos do cluster e acumula as carateristicas de cada exemplo na lista 'vals'
    Depois divide cada valor acumulado pelo numero de exemplos para obter a media das carateristicas e cria um novo exemplo centroid"""
    def computeCentroid(self):
        vals = [0.0] * self.examples[0].dimensionality()
        for e in self.examples:
            vals = [vals[i] + e.getFeatures()[i] for i in range(len(vals))]
        centroid = Example('centroid', [v/len(self.examples) for v in vals])
        return centroid
    
    """Retorna o centroide do cluster"""
    def getCentroid(self):
        return self.centroid
    
    """calcula a variedade do cluster, itera sobre os exemplos do cluster e calcula a distância Euclidiana ao quadrado entre cada exemplo 
    e o centróide. Em seguida, retorna a soma das distâncias ao quadrado."""
    def variability(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
    
    """Gerador que itera sobre os exemplos do cluster. A cada iteração, produz um exemplo."""
    def members(self):
        for e in self.examples:
            yield e
   
    """  retorna uma representação em string do cluster. Ele obtém os nomes dos exemplos, os ordena em ordem alfabética 
    e cria uma string que contém o centróide do cluster e os nomes dos exemplos separados por vírgula. 
    Em seguida, remove a vírgula e o espaço em branco no final da string e a"""
    def __str__(self):
        names = [e.getName() for e in self.examples]
        names.sort()
        result = 'Cluster with centroid ' + str(self.centroid.getFeatures()) + ' contains:\n '
        for e in names:
            result = result + e + ', '
        return result[:-2] # remove trailing comma and space