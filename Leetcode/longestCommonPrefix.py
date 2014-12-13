class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ''
            
        if len(strs) == 1:
            return strs[0]
            
        if len(strs[0]) == 0:
            return ''
        
        for i in range(len(strs[0])): # loop over the length of the first string
            for j in range(len(strs)-1): # loop over the other strings
                if i > len(strs[j+1])-1 or strs[j][i] != strs[j+1][i]:
                    return strs[0][0:i]

        return strs[0]
