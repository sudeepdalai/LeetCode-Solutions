# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        result = []
        q = [root]
        result.append([root.val])
        
        while q:
            temp = []
            while q:
                cur = q.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            if temp:
                q.extend(temp)
                result.append([node.val for node in temp])
        
        return result
