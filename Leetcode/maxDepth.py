'''
https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):

    	# in order traversal while saving the depth 

    	# recursive solution
    	# when given a tree find it's maxDepth and return it
			# when the tree has no child return 1
			# when the tree has 1 return : maxDepth on it + 1
			# when the tree has 2 return : max(maxDepth on each ) +1

		if root is None:
			return 0

		elif root.left is None or root.right is None:
			return self.maxDepth(root.left) + self.maxDepth(root.right) + 1

		else:
			return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

				
s = Solution()

test1 = TreeNode(10)
test2 = TreeNode(3)
test2.left = TreeNode(2)

test3 = TreeNode(3)
test3.left = TreeNode(2)
test3.left.left = TreeNode(1)
test3.right = TreeNode(4)
