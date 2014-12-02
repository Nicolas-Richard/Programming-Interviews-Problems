
# My first idea was to say that the tree is balanced if the leaves are all two consecutive levels (n and n+1). So I've build the method leafLevelTraversal, that outputs the level of every leaf.
# But it gets a Time Limit Exceeded on LeetCode, apparently because of the recursive calls.
# The second idea is about finding the depths of left and right subtrees iteratively. See : https://oj.leetcode.com/discuss/12491/runtime-error-for-python


#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = Non

class Solution:
# @param root, a tree node
# @return a boolean
    def isBalanced(self, root):

        if(root==None):return True
        l=self.getNodeDepth(root.left)
        r=self.getNodeDepth(root.right)

        return (abs(l-r)<2) and self.isBalanced(root.left) and self.isBalanced(root.right) # because you can have a depth difference <2 , but one of the tree might still be unbalanced


    def getNodeDepth(self, node):
        if(node==None):return 0

        stack=[(node,1)]
        dep=1

        while(len(stack)): # Find the depth of a tree iteratively
            first,dep=stack.pop(0)
            if(first.left!=None):
                stack.append((first.left,dep+1))
            if(first.right!=None):
                stack.append((first.right,dep+1))
        return dep;

        

'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):

    	if root == None:
    		return True
        
        lst = self.leafLevelTraversal(root)
        return (max(lst) - min(lst)) < 2

    def leafLevelTraversal(self,root, lst=[], level=0):  
    	# it really is no more than a in order traversal, that only outputs results for leaves and keep tracks of the level too.  	

    	if root.left != None:
    		self.leafLevelTraversal(root.left, lst,level+1)

    	if root.left == None and root.right == None:
    		#lst.append((root.val, level)) # Here I return both the level and the value of each node
    		lst.append(level) # Here I return only the level

    	if root.right != None:
    		self.leafLevelTraversal(root.right, lst,level+1)    	

    	return lst
'''




t = TreeNode(2)
t.left = TreeNode(1)
t.left.left = TreeNode(0.5)
t.left.left.left = TreeNode(0.2)
t.left.right = TreeNode(1.5)
t.right = TreeNode(3)

s = Solution()