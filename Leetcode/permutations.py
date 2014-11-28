
# Given a collection of numbers, return all possible permutations.

# I first built a recursive method which given an integer, return all possible permutation for the set of integer in range(1,n+1). It's the method permute1toN
# I had a hard time adapting this method to list of 'things'. I divided the problem, by first building the helper function insertPermute which given a list and an element to insert returns all the possible permutations of the elements of the list plus the new element;
# Given this I was able to build the recursive method that solves the problem. Note that in between permute1toN() and permute() the orders of the loops have been inverted.

#https://oj.leetcode.com/problems/permutations/

import copy

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
    	
    	if len(num) == 1:
    		return [num]
    	result = []	
    	for lst in self.permute(num[:-1]):
    		result += self.insertPermute(lst,num[-1:][0])
    	return result	

    # @param lst, a list of things
    # @param element_to_insert, a thing
    # @return a list of lists of things
    def insertPermute(self, lst, element_to_insert):
    	result=[]
    	copy_lst = []
    	for i in range(len(lst)+1):
    		copy_lst = copy.copy(lst)
    		copy_lst.insert(i,element_to_insert)		
    		result.append(copy_lst)
    	return result

    # @param num, an integer
    # @return a list of lists of integers
    def permute1toN(self, num):        
        if num ==1:
        	return [[1]]
        else:
        	result=[]
        	for i in range(0,num):
        		lst = self.permute1toN(num-1)
        		for l in lst:
        			l.insert(i,num)
        			result.append(l)
        return result



s=Solution()        