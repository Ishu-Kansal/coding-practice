class Solution:


    def minOperations(self, nums: List[int]) -> int:
        def coinChange(valIn: int) -> List[int]:
            # assume coins of vals 2 and 3
            # return minimum number of "coins" to fit into int
            if(valIn < 2):
                return [1, 1, 1]
            if(valIn == 2 or valIn == 3):
                return [1, 1, 1, 1]
            minOps = float('inf')
            dp = [1] * (valIn + 1)

            for i in range(4, valIn+1):
                dp[i] = min(dp[i-2], dp[i-3]) + 1
            return dp

        coins = {}
        totalOps = 0
        for num in nums:
            coins[num] = coins.get(num, 0) + 1
        maxVal = -1
        for numeric, count in coins.items():
            if(count > maxVal):
                maxVal = count
        
        fullDP = coinChange(maxVal)

        for numeric, count in coins.items():
            if(count < 2):
                return -1
            totalOps += fullDP[count]
        
        return totalOps