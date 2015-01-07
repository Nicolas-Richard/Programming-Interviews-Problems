'''
Doesn't pass the OJ for you don't return anything and OJ seems not to always pick
the right thing for his tests, a lot of people have the problem on the forum. 
Also learnt the solution in O(n), but can only work on arrays, go through the end
and place the elements at their right position (since you know the size of the 
final array), in order to make it work in Python would require you build an empty
list.

https://oj.leetcode.com/problems/merge-sorted-array/
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        
        # merge B into A
         # look at A[0]
         # find it's place in B. insert there using A.insert()

        if m == 0:
        	A += B
        	return

        for elem in B: # n elements
        	i = 0
        	while i < len(A): # up to m constant time operations => O(mn)
        		if A[i] < elem:
        			i += 1
        		else:
        			break	
 		
        	A.insert(i, elem)
        	return
        	
s = Solution()

A = [1]
B = [2]
s.merge(A,1,B,1)

C = []
D = [2]

s.merge(C,0,D,1)


''' # tests used when there is with 'return A'
print s.merge([1], 1,[2],1) == [1,2]
print s.merge([1], 1,[2,3],1) == [1,2,3]
print s.merge([1,4], 1,[2,3],1) == [1,2,3,4]
print s.merge([-1], 1,[2],1) == [-1,2]
print s.merge([], 1,[1],1) == [1]
'''

        			


