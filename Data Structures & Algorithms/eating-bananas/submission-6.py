class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        minTimeToEat = float('inf')
        while(minK <= maxK):
            print('eval', minK, maxK)
            mid = (minK + maxK + 1) // 2
            minTimeToEat = 0
            for pile in piles:
                minTimeToEat += math.ceil(pile / mid)
            
            if(minTimeToEat > h):
                minK = mid + 1
            else:
                maxK = mid - 1

        return minK