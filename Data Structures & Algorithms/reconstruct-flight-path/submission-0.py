class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # source = JFK

        # all tickets were used once

        # so we can construct a continuously connecting graph of directed edges

        # we can connect a graph of the tickets
        # with the airports as nodes, with JFK as the starting source
        # we want to find one none backtracking path that visits all airports 

        # if multiple paths exist, take the one smallest letter

        # the point is to use every ticket

        # need to visited all "tickets" so we need to visit all edges

        # which is eucliean path, not hamiltonain as hamiltonian is visiting all nodes
        # and we want to use all ticket exactly once

        graph = {}
        for ticket in tickets:
            start = ticket[0]
            end = ticket[1]
            if start not in graph:
                graph[start] = []
            
            graph[start].append(end)
        
        for start in graph:
            graph[start].sort()
        
        path = []
        stack = deque()
        stack.append("JFK")

        print(graph)

        while stack:
            u = stack[-1]
            # print(graph)
            
            if u in graph and len(graph[u]) != 0:
                v = graph[u].pop(0)
                stack.append(v)
            else:
                # No more outgoing edges from u → add to path
                path.append(stack.pop())

        print(path)
        path.reverse()
        return path