#Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ans=[]
        return self.helper(root, ans)
    
    def helper(self, root, lst=[]):    
                
        if  root.left != None:
            self.helper(root.left,lst) 

        lst.append(root.val)        
  
        if root.right != None:
            self.helper(root.right,lst) 

        return lst  


    def levelOrder(self, root):

        stack=[]
        result=[]
        dict={}
        stack.append(root)
        stack.append(0)
        level=0
        while len(stack)>1:
            
            level=stack.pop()
            tmp=stack.pop()
            
            if level not in dict.keys():
                dict[level]=[]

            if tmp!=None:
                dict[level].append(tmp.val)

                if tmp.right!=None:
                    stack.append(tmp.right)
                    stack.append(level+1)
            
                if tmp.left!=None:
                    stack.append(tmp.left)
                    stack.append(level+1)
        
        for key in dict:
            result.append(dict[key])

        return result        

s=Solution()

t=TreeNode(2)
t.left=TreeNode(1)
t.right=TreeNode(3)
t.left.left=TreeNode(0.5)
t.left.right=TreeNode(1.5)

