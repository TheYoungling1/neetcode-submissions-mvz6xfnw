class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # update the adjaceny list to keep track at every node visited at one dfs, so the second dfs dont count them again 

        # i.e. with every node in the CC reached, we remove the edges to its parent 

        # need to look through

        # loop through all nodes in the adjancey list, add 1 if that node is "1"
        map = {}

        for i in range(n):
            map[i] = []
        for edge in edges:
            u = edge[0]
            v = edge[1]

            map[u].append(v)
            map[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for n in map[node]:
                if n not in visited:
                    dfs(n)        

        counter = 0    
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)

        return counter

            



            
