# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    1. Iterative Solution
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append(((node.left, False)))

        return res

    """
        2. Recursive Solution
    """

    def helper(self, root, result):
        if root:
            self.helper(root.left, result)
            self.helper(root.right, result)
            result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result
