'''
https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''



# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):

        if root == None or root.val == None:
    		return []

    	levels = self.levelOrder(root)

    	mydict = {}

    	for element in levels:
    		mydict[element[1]] = []

    	for element in levels:
    		mydict[element[1]].append(element[0])

    	keys = mydict.keys()
    	keys.sort()

    	result = []

    	for key in keys:
    		result.insert(0,mydict[key])

    	return result
        
    def levelOrder(self, root, level = 0): 

        if not root:
        	return []

        return self.levelOrder(root.left, level + 1) + [(root.val, level)] + self.levelOrder(root.right, level +1)		

s = Solution()

tree = TreeNode (2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)     

print s.levelOrderBottom(tree) == [[1, 3], [2]]

tree2 = TreeNode(None)
print s.levelOrderBottom(tree2) == [[]]
