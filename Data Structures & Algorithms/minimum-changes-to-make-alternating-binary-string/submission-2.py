class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            if(int(s[i]) != i % 2):
                count += 1
        
        newCount = 0
        for i in range(0, len(s)):
            if(int(s[i]) == i % 2):
                newCount += 1
        
        return min(count, newCount)