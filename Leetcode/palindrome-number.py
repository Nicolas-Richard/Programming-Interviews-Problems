#https://oj.leetcode.com/problems/palindrome-number/
#http://en.wikipedia.org/wiki/Palindrome

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        # This solution uses 2 extra spaces
        if x<0:
            tmp2=-x
        else:
            tmp2=x
        tmp=0
        while tmp2!=0:
            tmp = tmp*10 + tmp2%10
            tmp2 = tmp2/10
        return x == int(tmp)


s=Solution()       