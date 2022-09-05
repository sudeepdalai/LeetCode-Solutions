# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p, q):
            if not p and not q:
                return True
            if p and q:
                return p.val == q.val and self.helper(p.left, q.left) and self.helper(p.right, q.right)
            
            return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if root is None and subRoot is not None:
            return False
        
        if self.helper(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
