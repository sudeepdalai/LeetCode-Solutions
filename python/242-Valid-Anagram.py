class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = [0] * 26
        tc = [0] * 26

        for ch in s:
            sc[ord(ch)-ord('a')] += 1

        for ch in t:
            tc[ord(ch)-ord('a')] += 1

        return sc == tc
