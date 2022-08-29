class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if this is the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                while (length + n) in num_set:
                    length += 1
                longest = max(length, longest)

        return longest
