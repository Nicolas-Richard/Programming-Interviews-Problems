'''
https://oj.leetcode.com/problems/integer-to-roman/
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        
        counter = 0
        result = ''

        while s >= 1:
        	result = self.convert(s%10, counter) + result
        	s = s/10
        	counter += 1

        return result	

    def convert(self, s, counter):

    	table = {}
        table[1,0] = 'I'
        table[5,0] = 'V'
        table[1,1] = 'X'
        table[5,1] = 'L'
        table[1,2] = 'C'
        table[5,2] = 'D'
        table[1,3] = 'M'

        if s == 0:
        	return ''

        elif s <= 3:
        	return table[1,counter]*s

        elif s == 4:
        	return table[1,counter] + table[5,counter]

        elif s <= 8:
        	return table[5, counter] + self.convert(s-5,counter)

        elif s == 9 :
        	return table[1,counter] + table[1,counter+1]

        elif s == 10:
        	return table[1,1]		

s = Solution()        	


'''
def convert1(self, s):

    	table = {}
        table[1] = 'I'
        table[5] = 'V'

        if s < 0:
        	return 

        elif s <= 3:
        	return table[1]*s

        elif s == 4:
        	return 'IV'

        elif s <= 8:
        	return table[5] + self.convert(s-5)

        elif s == 9 :
        	return 'IX' 	

    def convert10(self, s):

    	table = {}
        table[1] = 'X'
        table[5] = 'L'

        if s < 0:
        	return 

        elif s <= 3:
        	return table[1]*s

        elif s == 4:
        	return 'XL'

        elif s <= 8:
        	return table[5] + self.convert(s-5)

        elif s == 9 :
        	return 'XC' 	
'''        	