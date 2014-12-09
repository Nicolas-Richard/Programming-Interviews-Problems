



graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}

def DFS_it(graph, startingnode, value):

    stack=[startingnode]
    visited=set()

    while len(stack) >0:
        node=stack.pop()
        if node == value:
            return True
        else:
            if node not in visited:
                for n in graph[node]:
                    stack.append(n)
                visited.add(node)
    return False
            
def DFTraversal_it(graph, startingnode):

    stack=[startingnode]
    visited=set()

    while len(stack) >0:
        node=stack.pop()
        if node not in visited:
            for n in graph[node]:
                stack.append(n)
            visited.add(node)
    
    return visited


def dfs_rec(graph,start,path = []):
    path = path + [start]
    for node in graph[start]:
        if node not in path:
            path = dfs_rec(graph, node,path)
    return path











