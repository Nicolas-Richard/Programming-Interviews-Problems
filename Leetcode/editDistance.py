
# I've wrote two methods, one using a dict, one using a numpy array (easier to visualize the constructoon of the edit distance table.)
# The method that uses a numpy array to store the Edit Distance Table won't be accepterd by Leetcode because Leetcode doesn't  seem to be able to import numpy


import numpy as np

class Solution:
    # @return an integer

		def minDistance(self, word1, word2):

			editDistanceTable={}
			for i in range(len(word1)+1):
				editDistanceTable[(i,0)]=i
			for j in range(len(word2)+1):
				editDistanceTable[(0,j)]=j

			for i in range(1,len(word1)+1):
			 	for j in range(1,len(word2)+1):
					substitution = 0
					if word1[i-1] != word2[j-1]:
						substitution = editDistanceTable[(i-1,j-1)] + 1 # Depending on your definition of the edit distance you may want to replace this one by a two.
					else:
						substitution = editDistanceTable[(i-1,j-1)]	
			
					editDistanceTable[(i,j)]=min(editDistanceTable[(i-1,j)]+1, editDistanceTable[(i,j-1)]+1,substitution) 
			print editDistanceTable
			return editDistanceTable[(len(word1),len(word2))]

'''    def minDistance(self, word1, word2):
    	editDistanceTable=np.zeros((len(word1)+1,len(word2)+1))
    	for i in range(len(word1)+1):
    		editDistanceTable[i][0]=i
    	for j in range(len(word2)+1):
    		editDistanceTable[0][j]=j

    	for i in range(1,len(word1)+1):
    		 for j in range(1,len(word2)+1):
    			substitution = 0
    			if word1[i-1] != word2[j-1]:
    				substitution = editDistanceTable[i-1][j-1] + 2
    			else:
    				substitution = editDistanceTable[i-1][j-1]	

    			editDistanceTable[i][j]=min(editDistanceTable[i-1][j]+1, editDistanceTable[i][j-1]+1,substitution) 

    	return editDistanceTable[len(word1)+1][len(word2)+1]'''


s=Solution()
