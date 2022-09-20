class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
                
            j,k = i+1, len(nums)-1
            
            while j < k:
                cur = a + nums[j] + nums[k]
                if cur == 0:
                    result.append([a, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif cur > 0:
                    k -= 1
                else:
                    j += 1
        
        return result
