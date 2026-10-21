class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        currElem = float('inf')

        for num in nums:
            if(num == currElem):
                count += 1
            else:
                if(count == 0):
                    currElem = num
                    count = 1
                else:
                    count -= 1
        
        return currElem