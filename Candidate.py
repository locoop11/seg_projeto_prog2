# 2022-2023 Programacao 2 LTI
# Grupo 027
# 54961 Daniela Rodrigues
# 60253 Hugo Silva

from Example import *

class Candidate(Example):
    def __init__(self, name, features, listWords):
        """
        Constructor for the Candidate class.

        Args:
            name (str): The name of the candidate.
            features (list): A list of candidate's features.
            listWords (list): A list of candidate's words.
        """
        super().__init__(name, features)
        self._listWords = listWords
    
    def getListWords(self):
        """
        Get the list of words for the candidate.

        Returns:
            list: The list of words for the candidate.
        """
        return self._listWords
        
        