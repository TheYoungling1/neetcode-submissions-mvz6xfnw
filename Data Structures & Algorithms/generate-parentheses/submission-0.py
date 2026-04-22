class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # 2 flags, 0 represent that it is a parenthese that wraps around eerything to its left, while 1 is just a standalone parenthese on its side
        
        
        res = []
        ans = []
        
        def backtrack(open_n, closed_n):
            

            if open_n == closed_n == n:
                res.append("".join(ans))
                return
            

            if open_n < n:
                ans.append("(")
                backtrack(open_n + 1, closed_n)
                ans.pop()
             

            if closed_n < open_n:
                ans.append(")")
                backtrack(open_n, closed_n + 1)
                ans.pop()
                
        backtrack(0, 0)
        return res


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
        
#         visited = [False]*len(nums)
#         res = []

#         def dfs(path):
#             if len(path) == len(nums):
#                 res.append(path.copy())    
#                 return

#             for i in range(len(nums)):
#                 if not visited[i]:
#                     visited[i] = True
#                     path.append(nums[i])
                    
#                     # 2. Explore: Move to the next level of the tree
#                     dfs(path)
                    
#                     # 3. Backtrack: "Undo" the choice to try a different number
#                     path.pop()
#                     visited[i] = False                 
        
#         dfs([])

#         return res


