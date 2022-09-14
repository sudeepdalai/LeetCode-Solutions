# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        result = 0
        
        def dfs(root, path):
            nonlocal result
            if root is None:
                return
            
            path[root.val] = 1 + path.get(root.val, 0)
            
            if not root.left and not root.right:
                n_odd = 0
                for v in path.values():
                    if v % 2 != 0:
                        n_odd += 1
                        if n_odd > 1:
                            break
                if n_odd <= 1:
                    result += 1 
            
            dfs(root.left, path)
            dfs(root.right, path)
            path[root.val] -= 1
        
        dfs(root, {})
        return result
