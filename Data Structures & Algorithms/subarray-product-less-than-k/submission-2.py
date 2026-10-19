class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count = 0
        currMult = 1
        while(right < len(nums)):
            if(currMult * nums[right] < k):
                # print('adding ', right - left + 1)
                count += (right - left + 1)
                currMult *= nums[right]
            else:
                currMult *= nums[right]
                while(left < right and currMult >= k):
                    currMult /= nums[left]
                    left += 1
                if(currMult < k):
                    count += (right - left + 1)

            right += 1
                
        return count