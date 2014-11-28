
# Dynamic programming solution, 
# https://oj.leetcode.com/problems/climbing-stairs/

class Solution:
    # @param n, an integer
    # @return an integer

    cache = {1:1, 2:2}

    def climbStairs(self, n):

        if self.cache.has_key(n):
            return self.cache[n]
        else : 
            self.cache[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.cache[n]    


s=Solution()            