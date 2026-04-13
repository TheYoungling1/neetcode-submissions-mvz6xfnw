# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# so this quesiton is one where the construction information is "bubbling" up

# That is the perfect way to describe it! "Bubbling up" (or bottom-up propagation) is the hallmark of Post-Order Traversal.

# In tree problems, information usually flows in two directions:

# Top-Down: You pass a "requirement" or "constraint" down (like max_so_far in the Good Nodes problem).

# Bottom-Up (Bubbling): You collect "facts" from the leaves and combine them as you return to the root.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            # the results from 
            left, right = dfs(root.left), dfs(root.right)
            # makes sure the left and right are already balanced themselves
            # and the height of the subtrees differ no greater than on
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        