'''
https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root):

        if root is None:
            return 0

        if root.left is None or root.right is None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1

        return min(self.minDepth(root.left),self.minDepth(root.right))+1         


s = Solution()

tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
tree.right.left = TreeNode(2.5)
tree.left.left = TreeNode(0.5)
tree.left.left.left = TreeNode(0.25)

test1 = TreeNode(10)            
test2 = None

test3 = TreeNode(1)
test3.left = TreeNode(2)

'''
    def minDepth(self, root):
        # a solution that works but doesn't get accepted by Leetcode, based on level order traversal
        if root == None: 
            return 0

        stack = self.level_order(root)
        min_d = stack[0]
        for element in stack:
            if element < stack [0]:
                min_d = element
        return min_d        

    def level_order(self, root, level = 1, stack = []):

        if root.left == None and root.right == None:
            stack.append(level)

        if root.left != None:
            self.level_order(root.left, level + 1, stack)

        if root.right != None:
            self.level_order(root.right, level + 1, stack)

        return stack  

'''


'''     # another accepted solution, the same as the first one but with a less compacted syntax
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.right is  None:
            return self.minDepth(root.left) + 1
        elif root.left is None:
            return self.minDepth(root.right) + 1
        else:
            return min (self.minDepth(root.left), self.minDepth(root.right))+1            

'''        
