# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # think in layers
        # find the righ more value in each layer

        queue = deque()
        queue.append(root)
        
        res = []
        while queue:
            # snapshot length
            level_len = len(queue)
            found_flag = False
            for _ in range(0, level_len):
                
                # we always want to add the right one first, so its found first
                node = queue.popleft()
                if node:
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                
                    if not found_flag:
                        found_flag = True
                        res.append(node.val)
        
        return res
                
                
