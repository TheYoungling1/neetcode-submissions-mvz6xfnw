# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Checks for all nodes in the tree?
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it can't contain a subRoot (unless subRoot is also empty)
        if not root:
            return False
        
        # 1. Check if the trees are identical starting from the current node
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. If not, recursively check the left and right children of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # check is subtree is contained by starting from one node
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are null, they are identical
        if not p and not q:
            return True
        # If one is null or values don't match, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check if left and right subtrees are also identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        