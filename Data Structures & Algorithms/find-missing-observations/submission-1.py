class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        currSum = sum(rolls)
        desiredSum = mean * (n + len(rolls))

        if(desiredSum - currSum < n):
            return []

        maxAvg = (currSum + n*6) / (n + len(rolls))
        if(maxAvg < mean):
            return []
        
        toAdd = desiredSum - currSum - n
        res = [1] * n
        i = 0
        while(toAdd > 0 and i < len(res)):
            thisAdd = min(5, toAdd)
            res[i] += thisAdd
            toAdd -= thisAdd
            i += 1
        if(toAdd > 0):
            return []
        return res
