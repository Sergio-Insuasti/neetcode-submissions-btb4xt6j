# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        
        def height(root):
            if root is None:
                return 0
            LHeight = height(root.left)
            RHeight = height(root.right)
            diameter = LHeight + RHeight

            maxDiameter[0] = max(maxDiameter[0], diameter)
            return 1 + max(LHeight, RHeight)

        height(root)
        return maxDiameter[0]
