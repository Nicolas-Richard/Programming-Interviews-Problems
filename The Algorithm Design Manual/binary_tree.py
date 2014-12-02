


"""def traversal(n):
	if n == None: 
		return
    print n.value
	traversal(n.left)
	traversal(n.right)
"""



class Node:

	def __init__(self, value):

		self.value = value
		self.right = []
		self.left = []
		self.parent =[]

	def __str__(self):

		result ='Node value : ' + str(self.value)
		
		if self.parent != []:
			result+='\nParent node value : ' + str(self.parent.value)			
		else:
			result+='\nNo parent'		

		if self.left != []:
			result+='\nLeft child value : ' + str(self.left.value)
		else:
			result+='\nNo left child'	

		if self.right != []:
			result+='\nRight child value : ' + str(self.right.value)
		else:
			result+='\nNo right child'	

		return result






a = Node(56)
b= Node(32)
c= Node(67)
d=Node(89)

a.left = b
a.right = c
b.parent = a
c.parent = a
d.parent = c
c.right = d


