# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sizePath(self, root):
        if root is None:
            return 0
        leftPath = 1
        rightPath = 1

        leftPath += self.sizePath(root.left)
        rightPath += self.sizePath(root.right)

        return max(leftPath, rightPath)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.sizePath(root)
        