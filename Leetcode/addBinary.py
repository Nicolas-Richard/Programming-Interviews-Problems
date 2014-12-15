'''https://oj.leetcode.com/problems/add-binary/'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        
        # idea 1 : write a translator to digit and use it
        
        # idea 2 : append zeros to the short string to see things more clearly
            # once they are aligned, just need to sum by keeping track of a carry
            # loop by the tail of the string with index i
            # do sum % 1
                # flag if carry
                # if flag raised, add carry to next one
                # else keep going
            # at the end check if need to insert 0 at the head    
        
        c = [] #holds the result
        carry = 0
        sum = 0
        
        if len(b) > len(a):
            return self.addBinary(b,a)
            
        while len(a) > len(b):
            b = '0' + b

        n = len(a)    
            
        for i in range(len(a)):
            sum = 0
            sum = (int(a[n-i-1]) + int(b[n-i-1]) + carry)%2
            if int(a[n-i-1]) + int(b[n-i-1]) + carry > 1:
                carry = 1
            else:
                carry = 0
            c.insert(0,sum)
       
        if carry == 1:
           c.insert(0,1)
    
        result = ''

        for i in range(len(c)):
            result += str(c[i])

        return result    

s = Solution()

print s.addBinary('1100','1')        