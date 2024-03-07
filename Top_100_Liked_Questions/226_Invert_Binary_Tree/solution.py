# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def changeNodes(self, root):
        if root:
            aux = root.left
            root.left = root.right
            root.right = aux
            self.changeNodes(root.left)
            self.changeNodes(root.right)
        return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        self.changeNodes(root)
        return head