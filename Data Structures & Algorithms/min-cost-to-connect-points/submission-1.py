class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # cost the manhattan distance between the 2 points

        # the "edges" are un-directed

        # if we run an algorithm like djikstra, the result will be the 
        # same no matter from which node we started

        # how do nwe construct an edge? 
        # for each node, we connect it with the rest of the nodes,
        # then calculate manhattan distance as the weight for that edge

        # we then pick out the lowest weight needed for reach all node from a node

        # graph = {}

        # for i in range(len(points)):
        #     u, v = points[i]
        #     if i not in graph:
        #         graph[i] = []

        #     for j in range(len(points)):
        #         if j == i:
        #             continue

        #         u_j, v_j = points[j]
        #         d = abs(u_j - u) + abs(v_j - v)
        #         graph[i].append((j, d))
        
        q = set()
        dist = []
        prev = []
        for i in range(len(points)):
            dist.append(float('inf'))
            prev.append(-1)
            q.add(i)

        # print(graph)
        
        # lets start from any node
        dist[0] = 0  
        while q:
            u = min(q, key=lambda x: dist[x])
            u_i = points[u][0]
            u_j = points[u][1]
            print(u)
            q.remove(u)
            
            # Relax neighbours still in q
            for v in range(len(points)):
                if v == u:
                    continue

                v_i = points[v][0]
                v_j = points[v][1]

                weight = abs(u_i - v_i) + abs(u_j - v_j)
                if v in q and weight < dist[v]:   # ← Prim's: just `weight`, not dist[u] + weight
                    dist[v] = weight
                    prev[v] = u
        
        print(dist)

        return sum(dist)
