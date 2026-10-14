class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            currTotal = prev + nums[i]
            maxVal = max(currTotal, maxVal, nums[i])
            prev = max(currTotal, nums[i])
        
        return maxVal