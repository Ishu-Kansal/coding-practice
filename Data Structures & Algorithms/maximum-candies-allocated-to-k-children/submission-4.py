class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if(sum(candies) < k):
            return 0

        def getMaxSat(candyArr, perPile):
            maxSat = 0
            for j in range(len(candyArr)):
                maxSat += candyArr[j] // perPile
            return maxSat
        
        largest = max(candies)
        smallest = 1
        opt = -1
        while(smallest <= largest):
            mid = (smallest + largest) // 2
            maxSat = getMaxSat(candies, mid)
            if(maxSat < k):
                largest = mid - 1
            else:
                opt = max(opt, mid)
                smallest = mid + 1

        
        return opt
        

            
        