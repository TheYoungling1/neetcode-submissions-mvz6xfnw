# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        res = []
        def helper(root, level):
            # add bfs all elements into a list, and take the last element
            # of each level
            if root is None:
                return

            if len(res) <= level:
                res.append([])
            
            res[level].append(root.val)

            helper(root.right, level + 1)
            helper(root.left, level + 1)
        
        helper(root, 0)
        final = []
        for level in res:
            final.append(level[0])
        
        return final