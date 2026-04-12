# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if the root is none, then not more place for p and q?
        # if root.left :
        #     return root


        # else:
        # if p or q < root and p or q > root

        # if p or q < root, search for that in the left subtree
        # if p or q > root, then search in the right subtree

        # if p or q smaller than root, then it has no way to be in the right side


        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)      
        else:
            return root

