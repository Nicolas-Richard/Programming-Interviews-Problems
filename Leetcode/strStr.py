'''https://oj.leetcode.com/problems/implement-strstr/'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        
        if needle not in haystack:
            return -1      
        
        counter = 0
        
        # idea 1 : double looop
        for i in range(len(haystack)-len(needle)+1):
            counter = 0
            for j in range(len(needle)):
                if needle[j] == haystack[i+j]:
                    counter +=1
                else:
                    break
            if counter == len(needle):
                return i

        return -1
        

s = Solution()

print s.strStr('aaaa','c')        