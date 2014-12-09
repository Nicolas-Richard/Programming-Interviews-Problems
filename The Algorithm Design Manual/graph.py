
class Node:
	def __init__(self,value):
		self.value=value
		self.adjacentNodes=[]

	def __str__(self):
		result=''
		for l in self.adjacentNodes:
			result+='\n' + str(l.value)

		return 'Value : ' + str(self.value) + '\nAdjacent nodes : ' + result	


def DFS_it(node ,value):

	stack=[node]
	visited = set()

	while len(stack)>0:
		node=stack.pop()
		print node.value
		if node not in visited:
			if node.value == value:
				return True
			else:
				visited.add(node)
				for n in node.adjacentNodes:
					stack.append(n)
	print visited
	return False				


def BFS_it(node, value):

	queue=[node]
	parent= None
	visited = set()

	while len(queue)>0:
		node=queue[0]
		print node.value
		queue.remove(queue[0])
		if node not in visited:
			if node.value == value:
				return True
			else:
				visited.add(node)
				for n in node.adjacentNodes:
					queue.append(n)

	result =[]			
	for n in visited:
		result.append(n.value)

	print result				
	return False			

def BFS_it_path(node, value):

	parent= None
	queue=[[node, parent]]
	visited = {}

	while len(queue)>0:
		node=queue[0][0]
		parent=queue[0][1]
		#print node.value
		queue.remove(queue[0])
		if node not in visited:
			if node.value == value:
				
				visited[node]=parent
				
				for n in visited:
					print n
					print 'Parent :'
					print visited[n]
					print '--------'

				return True
			else:
				visited[node]=parent
				#visited.add(node)
				for n in node.adjacentNodes:
					queue.append([n,node])

			
	#for n in visited:
	#	print n
	#	print visited[n]

					
	return False	

"""
def DFS(node, value, processed=set(), discovered=[]):
	if node.value==value:
		return True

	elif node in processed:
		if discovered != []:
			DFS(discovered[0],value,processed,discovered.remove(discovered[0]))
		else:
			return False

	else:
		for n in node.adjacentNodes:
			discovered.append(n)
		processed.add(n)
		print '\n' + str(processed)
		print '\n' + str(discovered)
		if discovered !=[]:
			DFS(discovered[0],value,processed,discovered.remove(discovered[0]))					
		else:
			return False

"""






# testing

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

a.adjacentNodes.append(b)
a.adjacentNodes.append(c)

b.adjacentNodes.append(a)
b.adjacentNodes.append(d)

c.adjacentNodes.append(a)
c.adjacentNodes.append(d)

d.adjacentNodes.append(b)
d.adjacentNodes.append(c)
d.adjacentNodes.append(e)

e.adjacentNodes.append(d)
