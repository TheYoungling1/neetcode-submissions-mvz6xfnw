class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combination is 


# def dfs(state):
#     if BASE_CASE(state):                    # Pillar 1: when do we save?
#         result.append(current.copy())
#         return
    
#     for choice in CHOICES(state):           # Pillar 2: what are the options?
#         if IS_VALID(choice, state):         # Pillar 3: which ones survive?
#             current.append(choice)          # Pillar 4a: CHOOSE
#             dfs(NEXT_STATE(state, choice))  # Pillar 4b: EXPLORE
#             current.pop()                   # Pillar 4c: UNDO


        res = []
        parts = []                          # closed over by dfs
        
        def dfs(start):
            # Pillar 1: base case
            if len(parts) == k:
                res.append(parts.copy())
                return
            
            # Pillar 2: choices — numbers from `start` to n
            for num in range(start, n + 1):
                parts.append(num)           # 4a: choose
                dfs(num + 1)                # 4b: explore (next must be > num)
                parts.pop()                 # 4c: undo
        
        dfs(1)
        return res
            