class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        res = []
        total_sum = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                total_sum += nums[i]
        
        for v, i in queries:
            prev = nums[i]
            nums[i] += v
            
            if prev % 2 == 0:
                if nums[i] % 2 == 0:
                    total_sum += (nums[i] - prev)
                else:
                    total_sum -= prev
            else:
                if nums[i] % 2 == 0:
                    total_sum += nums[i]

            res.append(total_sum)
               
        return res
