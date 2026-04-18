"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # mayben use a dfs / bfs algorithm to traverse the graph
        # anc create a copy somehow during the traversal, whether in the 
        # bubbling down phase or the reconstruction phase
        
        # we can do a bfs 
        
        if not node:
            return None
            
        old_to_new = {}

        def dfs(node):
            # Base case: If we've already cloned this node, return the clone.
            if node in old_to_new:
                return old_to_new[node]
            
            # 1. Create the clone
            copy = Node(node.val)
            
            # 2. Add it to our hash map IMMEDIATELY before recursing.
            # This prevents infinite loops if a neighbor points back to this node.
            old_to_new[node] = copy
            
            # 3. Recurse through all neighbors and append the returned clones
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        # Kick off the recursion from the start node
        return dfs(node)


            
            