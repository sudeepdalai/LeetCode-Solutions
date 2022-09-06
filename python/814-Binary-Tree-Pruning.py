# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def contains_1(root):
            if not root:
                return False
            
            left = contains_1(root.left)
            right = contains_1(root.right)
            
            if not left:
                root.left = None
            
            if not right:
                root.right = None
            
            return root.val == 1 or left or right
    
        if contains_1(root):
            return root
        else:
            return None
