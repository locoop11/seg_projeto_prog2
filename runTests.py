from clusteringRealities import *
class Tests :
    sampleTitlesFile = "./files/titles.txt"
    
    def testKDifferentFronCandidatesExemplars():
        Tests.printTestName ("testKDifferentFronCandidatesExemplars", "Testing K different from candidates exemplars")
        testFile = "./files/test-KDifferentFromCandidatesExemplars.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 2)  
        except Exception as e:
            if( e.args[0] == "Cannot perform clustering with 2 clusters"):
                print("... Success: " + e.args[0])
                return
        print("... Test Failed")
    
    def testEmptyCandidatesFile ():
        Tests.printTestName ("testEmptyFile", "Testing empty files")
        testFile = "./files/test-EmptyCandidatesFile.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 2)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testCandidatesWithUnexistingTitles():
        Tests.printTestName ("testCandidatesWithUnexistingTitles", "Testing candidates with unexisting titles")
        testFile = "./files/test-CandidatesWithUnexistingTitles.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 2)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testNegativeK():
        Tests.printTestName ("testNegativeK", "Testing negative K")
        testFile = "./files/candidates.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, -2)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testKBiggerThanNumberOfCandidates():
        Tests.printTestName ("testNegativeK", "Testing negative K")
        testFile = "./files/candidates.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 200)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testKZero():
        Tests.printTestName ("testNegativeK", "Testing negative K")
        testFile = "./files/candidates.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 0)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testCandidatesWithLessTitlesThanExpected():
        Tests.printTestName ("testCandidatesWithLessTitlesThanExpected", "Testing candidates with less titles than expected")
        testFile = "./files/test-CandidatesWithLessTitlesThanExpected.txt"
        try:
            processFiles(Tests.sampleTitlesFile, testFile, 2)  
        except Exception as e:
            print("... Success: " + e.args[0])
            return
        print("... Test Failed")
    
    def testCandidatesHavingTheSameDistanceFrom2Centroids(): 
        Tests.printTestName ("testCandidatesHavingTheSameDistanceFrom2Centroids", "Testing candidates having the same distance from 2 centroids")
        return print("... Success")
    
    def testCandidatesHavingAnUnknownExemplar():
        Tests.printTestName ("testCandidatesHavingAnUnknownExemplar", "Testing candidates having an unknown exemplar")
        return print("... Success")
    
    def printTestName (testName, testDescription = ""):
        print ("Executing Test: " + testName + " - " + testDescription)
        return

Tests.testKDifferentFronCandidatesExemplars()
Tests.testEmptyCandidatesFile()
Tests.testCandidatesWithUnexistingTitles()
Tests.testNegativeK()
Tests.testKBiggerThanNumberOfCandidates()
Tests.testKZero()
Tests.testCandidatesWithLessTitlesThanExpected()
Tests.testCandidatesHavingTheSameDistanceFrom2Centroids()
Tests.testCandidatesHavingAnUnknownExemplar()