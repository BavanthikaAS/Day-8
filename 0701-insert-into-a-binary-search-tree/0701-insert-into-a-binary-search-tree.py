# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        root1=root
        while(True):
            if root1.val<val:
                if root1.right:
                    root1=root1.right
                else:
                    root1.right=TreeNode(val)
                    break
            else:
                if root1.left:
                    root1=root1.left
                else:
                    root1.left=TreeNode(val)
                    break
        return root