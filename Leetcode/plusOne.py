'''

The iterative solution was accepted by Leetcode.
The recursive solution wasn't even though I tested it on a virtual environment on Python 2.7 and it worked fine.
https://oj.leetcode.com/problems/plus-one/
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits, carry_flag = False):
        
        # [1,2,3] => [1,2,4]
        # where it's tricky is when we have a carry to pass along
        
        # loop from the tail of the list to the top
        # add one at the tail, if carry, the carry_flag goes true and while carry_flag is true we move up to the head of the list
        # special case, if we reach the head with a carry must add an element to the list. we can check for this case with the index going == len(list)
        
        # recursion ? call the function on a slice of the list ?
            # when there is a carry, it's like calling plusone on the other element.
            # how to handle the last case ? I know I'm on the last case if I'm given a void list / list with 1 element
            # do I still raise a flag when I have a carry ?
            # need to pass the cary flag along
            # how do I make the changes last on the actual list while moving around slices ?
            
        n = len(digits)
        
        if n == 0 and carry_flag == True:
            print 'here'
            digits.insert(0,1)
            carry_flag = False
        elif n == 0 and carry_flag == False:
            return digits    

        if carry_flag == True:
            print 'here2'
            digits[n - 1] = (digits[n - 1] + 1)%10
            if digits[n - 1] == 0:
                carry_flag = True
            else:
                carry_flag = False      

        if carry_flag == True:
            return self.plusOne(digits[:n-1], carry_flag == True) +  digits[n-1:]
        else:
            return digits    
            
        return digits    

s = Solution()

print s.plusOne([0], True)           

'''
    def plusOne_iterative(self, digits):
        
        n = len(digits)
        carry_flag = True
        
        i=0
        while carry_flag == True and i < n:
            digits[n-i-1] = (digits[n-i-1] + 1)%10
            if digits[n-i-1] == 0:
                carry_flag = True
            else:
                carry_flag = False
            i+=1
        
        if carry_flag == True:
            digits.insert(0,1)

        return digits   

'''
