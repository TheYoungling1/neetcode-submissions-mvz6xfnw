# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque() 
        queue.append(root)
        
        res = []
        
        # layer loop
        while queue:
            level = []
            # take a snapshot of the nodes currently in the dequeue
            # so we dont add in the children in the same layer

            q_len = len(queue)
            print(q_len)
            for i in range(0, q_len):
                value = queue.popleft()
                if value:
                    level.append(value.val)
                    if value.left:
                        queue.append(value.left)
                    
                    if value.right:
                        queue.append(value.right)
            if level:
                res.append(level)
        # res.pop()
        return res

