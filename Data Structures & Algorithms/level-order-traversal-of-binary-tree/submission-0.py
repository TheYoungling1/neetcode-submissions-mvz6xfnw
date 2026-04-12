# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # track what layer the node is on, and add to the list accordingly

        res = []

        def levelOrderRec(root, level):
            # Base case
            if root is None:
                return

            # Add a new level to the result if needed
            if len(res) <= level:
                res.append([])

            # Add current node's data to its corresponding level
            res[level].append(root.val)

            # Recur for left and right children
            levelOrderRec(root.left, level + 1)
            levelOrderRec(root.right, level + 1)

        levelOrderRec(root, 0)
        return res

