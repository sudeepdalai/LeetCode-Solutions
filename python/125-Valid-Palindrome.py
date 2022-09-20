class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = [x.lower() for x in s if x.isalnum()]
        i, j = 0, len(clean_str)-1
        
        while i<j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
