class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        
        while len(h) > 1:
            s1 = -1 * heapq.heappop(h)
            s2 = -1 * heapq.heappop(h)
            res = s1 - s2
            if res > 0:
                heapq.heappush(h, -1 * res)
        
        if h:
            return abs(h[0])
        else:
            return 0
