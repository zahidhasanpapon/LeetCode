# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    1. Recursive Solution
    """

    def traverse(self, root, preorderTraversalArray):
           if root is None:
                return
            preorderTraversalArray.append(root.val)
            self.traverse(root.left, preorderTraversalArray)
            self.traverse(root.right, preorderTraversalArray)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorderTraversalArray = []
        self.traverse(root, preorderTraversalArray)
        return preorderTraversalArray

    """
    2. Iterative Solution
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorderTraversalArray = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                preorderTraversalArray.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return preorderTraversalArray
