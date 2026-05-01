class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        
        visited = {"0000"}
        # bfs queue
        queue = deque([("0000", 0)])  # (state, moves)
        
        while queue:
            state, moves = queue.popleft()
            
            # Generate 8 neighbors
            # for each layer
            for i in range(4):
                # decides if to increase it by one or decrease it
                for delta in (-1, 1):
                    new_digit = (int(state[i]) + delta) % 10
                    neighbor = state[:i] + str(new_digit) + state[i+1:]
                    
                    if neighbor == target:
                        return moves + 1
                    if neighbor not in dead and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, moves + 1))
        
        return -1