class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        longestLen = 0
        
        while(len(numSet) > 0):
            initial = next(iter(numSet))
            numSet.remove(initial)
            left = initial - 1
            right = initial + 1
            currLen = 1
            while(left in numSet or right in numSet):
                if(left in numSet):
                    currLen += 1
                    numSet.remove(left)
                    left -= 1
                    
                if(right in numSet):
                    currLen += 1
                    numSet.remove(right)
                    right += 1

            longestLen = max(longestLen, currLen)
        
        return longestLen