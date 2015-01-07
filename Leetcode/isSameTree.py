'''
https://oj.leetcode.com/problems/same-tree/
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        
        # idea 1 : recursion
        	#check the value for the root, if true keep going (return) with the two child node

        # idea2 : iterative
        	# traversal that keeps track of the empty leaves. Flatten the tree to a list representation

        if p == None and q == None:
        	return True
        elif p == None or q == None:
        	return False
      	elif p.val == q.val: 
      		return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
      	else : 
      		return False


s = Solution()

p = TreeNode(2)

print s.isSameTree(None,None) == True

print s.isSameTree(p,None) == False

print s.isSameTree(p,p) == True

p.left = TreeNode(1)
p.right = TreeNode(3)

print s.isSameTree(p,p) == True



