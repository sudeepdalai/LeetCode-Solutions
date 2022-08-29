import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.solution2(nums, k)

    def solution1(self, nums, k):
        '''
        sorting frequency dict approach
        '''
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        sf = sorted(freq, key=freq.get, reverse=True)
        return sf[:k]

    def solution2(self, nums, k):
        '''
        modified bucket sort approach
        '''
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, val in count.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
