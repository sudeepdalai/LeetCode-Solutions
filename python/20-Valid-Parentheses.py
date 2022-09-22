class Solution:
    def isValid(self, s: str) -> bool:
        bkts = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for b in s:
            if b not in bkts:
                stack.append(b)
                continue
            else:
                if not stack or stack[-1] != bkts[b]:
                    return False
                stack.pop()
        
        return len(stack) == 0
