class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calcSquareSum(num: int):
            total = 0
            while(num > 0):
                currDigit = num % 10
                num //= 10
                total += currDigit * currDigit
            return total
        
        seen = set()
        thisSum = calcSquareSum(n)
        while(thisSum != 1):
            thisSum = calcSquareSum(thisSum)
            if(thisSum in seen):
                return False
            if(thisSum == 1):
                return True
            seen.add(thisSum)
        
        return True