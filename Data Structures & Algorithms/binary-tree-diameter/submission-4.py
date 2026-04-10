# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Establish the persistent variable attached to the class instance
        self.curr_max = 0
        
        # Define the helper function inside the main function (or as another class method)
        def max_depth(node):
            if not node:
                return 0
            
            # Recursively get the depth of the left and right subtrees
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            
            # Check if the diameter passing through THIS node is the biggest we've seen
            if left_depth + right_depth > self.curr_max:
                self.curr_max = left_depth + right_depth
                
            # Return the depth of this subtree to the parent node
            return 1 + max(left_depth, right_depth)
        
        # Kick off the recursion from the top root
        max_depth(root)
        
        # Return the maximum diameter found
        return self.curr_max
            

