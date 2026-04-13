# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # for each recursion, function(root, current value)
        # ^ will not work, because if the 1 had 0 and 4 as child
        # will still get counted as valid even though 4 > 2

        # or at each node, we check if the children are both less than the big root


        # for a right child on the right subtree, the min is the parent node, max is infiite
        # for a left child on the right subtree, the min would have to be the "head", the max would be the parent node
        
        # for a left on the left subtree, the max is the parent node, the min is infinit
        # for a right on the left subtree, the max is the "head" of the tree, the min is the parent

    
        def bstHelper(root, max_val, min_val):
            if root is None:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return bstHelper(root.left, root.val, min_val) and bstHelper(root.right, max_val, root.val)

        
        return bstHelper(root, float('inf'), float('-inf'))