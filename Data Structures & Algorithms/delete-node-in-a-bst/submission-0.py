# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if root.left is None:
                return root.right  # handles Case 1 (both None) and Case 2
            if root.right is None:
                return root.left
            
            # Case 3: two children — find inorder successor, the leftest child of the right
            # subtree, the closest numerically to the deletion node
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # set
            root.val = successor.val
            # call itself to remove the leftest child
            root.right = self.deleteNode(root.right, successor.val)
        
        return root