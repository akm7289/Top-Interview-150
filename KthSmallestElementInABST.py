class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def modifiedDFS(self, node, k):
        if node==None:
            return k,node
        if node.left:
            k,_ = self.modifiedDFS(node.left, k)
        k = k + 1
        node.val = [node.val,k]
        if node.right:
            k,_ = self.modifiedDFS(node.right, k)
        return k,node
    def findkthElement(self,node,k):
        if not node:
            return
        if node.val[1]==k:
            return node.val[0]
        elif node.val[1]>k:
            return self.findkthElement(node.left,k)
        else:
            return self.findkthElement(node.right,k)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        _,tree=self.modifiedDFS( root, 0)
        return self.findkthElement(tree,k)
if __name__=='__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = None
    root.right.right = None
    root.left.left.left = TreeNode(1)
    root.left.left.right = None
    result=Solution().kthSmallest(root,3)
    print(result)

