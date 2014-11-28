# Think of reducing the problem to a smaller array, and see how you can get the result for the acutal array if you have the answer on this smaller arrayay

# https://oj.leetcode.com/problems/maximum-subarray/
# http://en.wikipedia.org/wiki/Maximum_subarray_problem

class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxSubArray(self, A):
        lst=[]
        lst.append(A[0])
        for i in range(1, len(A)):
        	lst.append(max(lst[i-1]+A[i], A[i]))

        return max(lst)	

s= Solution()