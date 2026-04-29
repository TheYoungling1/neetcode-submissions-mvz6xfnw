import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list (1-indexed, so size n+1)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # dist[i] = shortest distance from k to i
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[k] = 0

        # Q = set of unvisited vertices
        queue = set(range(1, n + 1))

        while queue:
            # Find vertex in queue with minimum dist — O(V) scan
            u = min(queue, key=lambda x: dist[x])
            
            # If the smallest dist is infinity, remaining nodes are unreachable
            if dist[u] == INF:
                break
            
            queue.remove(u)

            # Relax edges to neighbors still in queue
            for neighbour, weight in graph[u]:
                if neighbour in queue:
                    alt = dist[u] + weight   # ADD, not multiply
                    if alt < dist[neighbour]:
                        dist[neighbour] = alt

        # Network delay time = time for signal to reach the LAST node
        # = maximum of all shortest distances
        max_dist = max(dist[1:])  # skip index 0 (unused)
        return max_dist if max_dist < INF else -1