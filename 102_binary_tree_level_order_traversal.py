# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursiveGoDown(self,node,level,levelsDictionary):
        if node:
            if not level in levelsDictionary:
                levelsDictionary[level]=[]
            levelsDictionary[level].append(node.val)
            if node.left:
                self.recursiveGoDown(node.left,level+1,levelsDictionary)
            if node.right:
                self.recursiveGoDown(node.right,level+1,levelsDictionary)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levelsDictionary={}
        if root:
            self.recursiveGoDown(root,0,levelsDictionary)
        output=[]
        for key,value in levelsDictionary.items():
            output.append(value)
        return output
