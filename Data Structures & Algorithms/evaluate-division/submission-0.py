class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
# Build the graph as a dict mapping each node to a list of (neighbor, weight) pairs
# For each query, run DFS with a visited set, carrying the accumulated product
# Handle the "unknown variable" case before doing anything else

        # Build bidirectional graph
        graph = {}
        for (src, tgt), w in zip(equations, values):
            if src not in graph: graph[src] = []
            if tgt not in graph: graph[tgt] = []
            graph[src].append((tgt, w))
            graph[tgt].append((src, 1 / w))
        
        def dfs(node, end, curr, visited):
            if node == end:
                return curr
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, curr * weight, visited)
                    if result != -1:
                        return result
            # no outgoing neighbours for this node
            return -1
        
        res = []
        for c, d in queries:
            # each search is independent
            if c not in graph or d not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(c, d, 1.0, set()))
        return res
