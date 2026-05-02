class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # connected graph without cycle -> tree

        # tree !+ BST
        # can have multiple nodes, dont gave to follow by 
        # left node < parent, right node > parent rule

        # we can do it the same as recursion on bst
        # instead of recursing on the left and right substree
        # we recurse on each neighbour
        # pass in the curr height as a parameters 
        # so each recursion can add to that individually

        # return recursion when no neigbhbours (end of tree)

        # (cycle on all starting nodes and find the max)?

        # is all MHT the same starting all ndoe?
        # i dont think so, because the edges are directed?

        if n == 1:
            return [0]
        
        # Build undirected graph
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, height, visited):
            visited.add(node)
            max_height = height
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    next_height = dfs(neighbor, height + 1, visited)
                    max_height = max(max_height, next_height)
            
            return max_height
        
        heights = []
        for root in range(n):
            heights.append(dfs(root, 0, set()))
        
        min_height = min(heights)
        return [i for i in range(n) if heights[i] == min_height]

        

        

