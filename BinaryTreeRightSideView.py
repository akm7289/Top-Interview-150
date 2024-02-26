# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfsLeftFirst(self, node, result, currentDepth=1):
        if not node:
            return
        if currentDepth > len(result):
            result.append(node.val)

        self.dfsLeftFirst(node.right, result, currentDepth + 1)
        self.dfsLeftFirst(node.left, result, currentDepth + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        self.dfsLeftFirst(root, result, currentDepth=1)
        return result
