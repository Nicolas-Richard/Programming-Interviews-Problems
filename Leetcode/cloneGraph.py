
'''

https://oj.leetcode.com/problems/clone-graph/

This solution is not optimal as it requires 2*n space. That's because before cloning I
put together new representation of the initial graph (dictionnary).

'''



# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        if node == None: 
            return None

        if node.neighbors == []:
            return UndirectedGraphNode(node.label)    

        visited = self.BFS(node) # the input graph is now easily accessible in this dict

        # print 'visited'
        # print visited.keys()

        new_nodes = {} # the new graph will be put together in this dictionnary

        for key in visited.keys(): # creating a each new node (without neighbors)
            new_nodes[key] = UndirectedGraphNode(key)
        
        # print 'new_nodes'
        # print new_nodes.keys()

        for key in visited: # adding neighbors
            list_of_neighbors = visited[key].neighbors
            
            for neighbor in list_of_neighbors:
                new_nodes[key].neighbors.append(new_nodes[neighbor.label])

        #for key in new_nodes:
        #    print '#'*25
        #    print 'label: %d' %(new_nodes[key].label)
        #    for neighbor in new_nodes[key].neighbors:
        #        print neighbor.label


        return new_nodes[node.label]



    def BFS(self, node):

        visited = {}
        to_visit = [node]

        while to_visit != []:
            current_node = to_visit.pop(0) # pop() for DFS
            if current_node.label not in visited:
                # regular graph traversal stuff
                visited[current_node.label] = current_node
                to_visit = to_visit + current_node.neighbors    
        
        #for key in visited:
        #    print visited[key].label 

        return visited

s = Solution()

'''# test 1
node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(3)

node0.neighbors.append(node1)
node0.neighbors.append(node2)
node1.neighbors.append(node2)
node2.neighbors.append(node3)
'''

# test 2
node0 = UndirectedGraphNode(-1)
node1 = UndirectedGraphNode(1)
node0.neighbors.append(node1)
