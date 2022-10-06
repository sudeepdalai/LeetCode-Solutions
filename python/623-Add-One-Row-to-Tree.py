# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        def dfs(root, prev_depth):
            if root is None:
                return
            
            prev_depth += 1
            if prev_depth == depth-1:
                lnode, rnode = TreeNode(val), TreeNode(val)
                lnode.left = root.left
                rnode.right = root.right
                root.left = lnode
                root.right = rnode
            
            dfs(root.left, prev_depth)
            dfs(root.right, prev_depth)
        
        dfs(root, 0)
        return root
