

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        
        if root == None:
            return False
        
        if root.val == sum:
            if root.left == None and root.right == None:
        	    return True
        
        if root.left != None: 
            if self.hasPathSum(root.left, sum - root.val) == True: # this is important
            		# I first made the mistake to just return the recursive call, but it doesn't 
            		# work because you don't get the chance to visit the right subtree
                return True
        if root.right != None:
            if self.hasPathSum(root.right, sum - root.val) == True:
            	return True
                
        return False
             
                
test1 = TreeNode(1)
test1.left = TreeNode(2)
test1.left.left = TreeNode(100)
test1.right = TreeNode(4)

s = Solution()

print s.hasPathSum(test1, 103)


# My thought process
        #idea 1 brute force, go to every possible leaf and check if the sum is the one I'm looking for
            # how to actually do that ? whar traversal ?
            # note : the example given is not a binary search tree
            # level order seem like it might a good idea
            
        # idea 2 : flatten the tree, should make it easier to search in the resulting lists if one is working    
        # idea 3 : recursive solution ? trees usually work well with recursion
        # after visiting a node call the solution on (node.next, x-node.value)
        # stop conditions : node.value == None
                        #   if node.val == x => return TRue



