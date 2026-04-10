# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we can see that for every root, we just want its children subtress swapped
        if root == None:
            return
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)

            tmp = root.right
            root.right = root.left
            root.left = tmp

            return root