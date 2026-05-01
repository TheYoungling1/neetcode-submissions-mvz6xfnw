# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # no if 2 directely linked house to any house is broken

        # i.e. if 2 and 3 are broken, then 4 is alamred
        # if 3 and 4 is broken, then 2 is alarmed

        # for each node, we need to know its parent, its 
        # left, and its right, becasue we can only do one

        # and we recurse on left and right and see whsts the best we can do
        # but whast about the parent?

        # my bad, so only 2 directed linked houses

        # so its about maximsing left, right of current node + its parent


        # if not root: return 0
        
        # # Option A: rob this node, skip children, take grandchildren
        # take = root.val
        # if root.left:
        #     take += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     take += self.rob(root.right.left) + self.rob(root.right.right)
        
        # # Option B: skip this node, take best from children
        # skip = self.rob(root.left) + self.rob(root.right)
        
        # return max(take, skip)


        def helper(node):
            if not node:
                return (0, 0)  # (rob_this, skip_this)
            
            L_rob, L_skip = helper(node.left)
            R_rob, R_skip = helper(node.right)
            
            rob_this  = node.val + L_skip + R_skip
            skip_this = max(L_rob, L_skip) + max(R_rob, R_skip)
            
            return (rob_this, skip_this)

        return max(helper(root))