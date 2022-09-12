import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        
        for x, y in points:
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(h, (-1 * dist, x, y))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for dist, x, y in h:
            res.append((x, y))
        
        return res
