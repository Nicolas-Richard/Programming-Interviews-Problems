
'''

This is a recursive solution, that goes one level to deep in defining the base case, 
therefore there are many cases to consider as you'll see in the helper function.

Much much maller recursive solution see isSymmetric2.py 
from : https://oj.leetcode.com/discuss/17707/recursive-and-non-recursive-solutions-in-python

https://oj.leetcode.com/problems/symmetric-tree/

'''

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

        # idea 1 : recursion
            # hard because I want to compare two trees, and my function actually just take one
                # therefore I can't make my recursive call
                # and because you are symmetric doesn't mean that the tree under you is

        # idea2 : iterative
            # level order traversal while keeping track of empty leaves
            # then check per level


        if root == None:
            return True

        if root.left == None and root.right == None:
            return True

        elif root.left == None or root.right == None:
            return False

        else:
            return self.helper(root.left, root.right)
    

    def helper(self, p, q): # p left subtree and q right subtree
        
        if p.val != q.val:
            return False
        else:
            pl = p.left
            pr = p.right
            ql = q.left
            qr = q.right

            quad = [pl,pr,ql,qr]
            quad_is_there_value = [pl != None, pr != None, ql != None, qr != None]

            #print quad_is_there_value
            #print quad

            if quad_is_there_value == [False, False, False, False]:
                return True

            elif quad_is_there_value.count(False) == 1 or quad_is_there_value.count(False) == 3:
                return False

            elif quad_is_there_value.count(False) == 2:
                if quad_is_there_value[0:2].count(False) == 0 or quad_is_there_value[0:2].count(False) == 2:
                    return False
                else: # need to identify the positions of 'True' and make a recursive call
                    true1 = quad_is_there_value[0:2].index(True)
                    true2 = quad_is_there_value[2:4].index(True) + 2

                    if (true1,true2) == (0,3) or (true1,true2) == (1,2):
                        return self.helper(quad[true1], quad[true2])
                    else:
                        return False

            elif quad_is_there_value.count(False) == 0:
            
                return self.helper(pl, qr) and self.helper(pr, ql)

                
s = Solution()

tree = TreeNode(1)

print s.isSymmetric(tree) == True

tree.left = TreeNode(2)
tree.right = TreeNode(3)

print s.isSymmetric(tree) == False

tree.right = TreeNode(2)

print s.isSymmetric(tree) == True

tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)

print s.isSymmetric(tree) == True

tree.right.right = TreeNode(4)

print s.isSymmetric(tree) == False

tree.right.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)

print s.isSymmetric(tree) == True

tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(8)

tree.right.right.left = TreeNode(8)
tree.right.right.right = TreeNode(7)

print s.isSymmetric(tree) == False



'''
            1
           / \
          2   2
         / \ / \
        3  4 4  3
     / \ / \ / \ / \
     5 6 7 8 8 7 6 5      

'''     