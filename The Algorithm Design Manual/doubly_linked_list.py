
#Doubly linked list

class Node:

	def __init__(self,value, right=None, left=None):
		self.value = value
		self.right = right
		self.left = left

	def __str__(self):
		result = 'Value : ' + str(self.value)
		if self.left != None:
			result+= '\nValue to the left : ' + str(self.left.value)
		else:
			result+= '\nNothing to left'
		if self.right != None:
			result+= '\nValue to the right : ' + str(self.right.value)
		else:
			result+= '\nNothing to right'

		return result		

	def append(self, value):
			
		while self.right != None:
			self = self.right

		self.right=Node(value)		
		self.right.left= self

	def delete(self, value):

		if self.value == value:
			#self.right.left= None
			#self=self.right
			# Trying to set the forst node = to the 2d doesn't work, because the variable that stores the first node, the head, still point to the old first node
			# but stealing the values of the second 2 node an putting them in the first one, allows to actually jump over the 2nd node while deleting the info of the first.


			self.value = self.right.value
			self.right= self.right.right
			self.left=None

			return


		while self.value != value:
			self = self.right

		if self.left != None:
			self.left.right = self.right

		if self.right != None :	
			self.right.left = self.left

 
 	def traversal(self):
 		while self!=None:

 			print self.value
 			self=self.right


lst = Node(1)
lst.append(2)
lst.append(3)
lst.append(4)

print lst
print 'Going through the list:'
lst.traversal()