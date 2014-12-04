
''' Given an array of strings, return all groups of strings that are anagrams.

Time Complexity :

N words of size at most M.
The upper bound is O(NMLogM + MNLogN).
http://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/


https://oj.leetcode.com/problems/anagrams/

'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        
        data = []
        for i in range(len(strs)): # O(N)
        	data.append([strs[i],''.join(sorted(strs[i]))]) # O(N*Mlog(M)) sorting a M characters word N times

        data.sort(key= lambda x : x[1]) # O(M*Nlog(N)) sorting N pairs of M characters. NlogN word to word comparison, each comparison is at most M operations.

        result = []

        for i in range(len(strs)): #O(n)
        	if i == 0: 
        		try : 
        			if data[i][1] == data[i+1][1]:
        				result.append(data[i][0])
        		except:
        			return []	# get rid off the case where len(strs)=1

        	elif i == len(strs)-1:
         		if data[i][1] == data[i-1][1]:
        			result.append(data[i][0])
        			
        	else:
        		if data[i][1] == data[i+1][1] or data[i][1] == data[i-1][1]:
        			result.append(data[i][0])		

       	return result

s = Solution()

