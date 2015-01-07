class Solution:
    # @return an integer
    def romanToInt(self, s):

        trans = {}
        trans['I'] = 1
        trans['V'] = 5
        trans['X'] = 10
        trans['L'] = 50
        trans['C'] = 100
        trans['D'] = 500                                
        trans['M'] = 1000
        
        total = 0

        for i in range(len(s)-1):
        	if trans[s[i]] < trans[s[i+1]]:
        		total -= trans[s[i]]
        	else:
        		total += trans[s[i]]

        total += trans[s[len(s)-1]]

        print total
        return total

solu = Solution()



print solu.romanToInt('III') == 3
print solu.romanToInt('VI') == 6
print solu.romanToInt('XV') == 15
print solu.romanToInt('CCXV') == 215
print solu.romanToInt('DCCXV') == 715
