class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # do this using a dfs approach
        # we can keep a track of the nodes we've alreadys fully vi

        # so to know if a graph it a valid tree, we just have to check for the following:

        # fails if a parent node is connecte to the child of its child node
        # fails if a parent's child node is connecred to another child node of its parent

        # so one way is to use a bfs, and keep track of all the node's we've seen so far, if a neighbour is a node already in 
        # the visited set, the return false

        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            # if i just do adj[u].append[v]
            # we just assume one direction in the edges, i. [0, 2] = 0 -> 2
            # but if we have [2, 0], that can also mean 0 -> 2, but our code counts it as 2 -> 0

        visit = set()
        # any invalid node is okay to start as parent, as any valid current node we only need to consider its neighbours anyways
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                # no need to worry about the parent node which is also a neighbour of the node
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n