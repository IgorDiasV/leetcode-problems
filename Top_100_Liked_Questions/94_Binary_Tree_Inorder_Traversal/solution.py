# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def orderedTree(self, tree: Optional[TreeNode], output: list[int]):
        if tree == None:
            return None
        self.orderedTree(tree.left, output)
        output.append(tree.val)
        self.orderedTree(tree.right, output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.orderedTree(root, output)
        return output
        