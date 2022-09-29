# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def bin_search(l, r):
            if l <= r:
                m = l + (r-l) // 2
                g = guess(m)
                if g == 0:
                    return m
                elif g == -1:
                    return bin_search(l, m-1)
                else:
                    return bin_search(m+1, r)
        
        return bin_search(0, n)
