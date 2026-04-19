

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

       # we can model this as a graph structure 

        # if there is a pre-req, model this as a directed edge

        # since the order of the numbers dont matter, given that there are no pre-reqs
        # we can take the courses in parallel, i.e. all 0-8 courses on the same time

        # so the only failures occur when there is a cycle in the graph
        # i.e. 1 -> 0 AND 0 -> 1?

        # construct the graph first

        graph = {}

        for pair in prerequisites:
            if pair[0] not in graph:
                graph[pair[0]] = []
            graph[pair[0]].append(pair[1])
        
        if not graph:
            return True

        # this means that the key node is the pre-req of all the neighbours

        state_tracker = [0]*(numCourses)

        def dfs(node):
            if state_tracker[node] == 1: # Cycle detected
                return False
            if state_tracker[node] == 2: # Already processed and safe
                return True
            
            state_tracker[node] = 1 # Mark as "Visiting"
            
            # Check if this node exists in our graph (some might not have neighbors)
            for neighbor in graph.get(node, []):
                # if one neighbour returned fals
                if not dfs(neighbor):
                    return False
                    
            state_tracker[node] = 2 # Mark as "Fully Visited"
            return True
        
        for node in graph:
            if not dfs(node):
                return False
        
        return True



        