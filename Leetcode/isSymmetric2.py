
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):

    	if not root:
    		return True
    	else:
    		return self.helper(root.left, root.right)	

    def helper(self, p, q): # given to tree p and q check if they are symmetric

    	if not p and not q:
    		return True

    	elif not p or not q:
    		return False

    	elif p.val == q.val:
    		return self.helper(p.left, q.right) and self.helper(p.right, q.left)
    	else :
    		return False	

s = Solution()

print s.isSymmetric(None) == True

tree = TreeNode(1)
			
print s.isSymmetric(tree) == True

tree.left = TreeNode(2)

print s.isSymmetric(tree) == False

tree.right = TreeNode(2)

print s.isSymmetric(tree) == True




