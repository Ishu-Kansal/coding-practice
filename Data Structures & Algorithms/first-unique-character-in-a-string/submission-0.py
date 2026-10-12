class Solution:
    def firstUniqChar(self, s: str) -> int:
        currCounts = [0] * 26
        firstIdx = [len(s)] * 26
        for i in range(len(s)):
            currCounts[ord(s[i]) - ord('a')] += 1
            if(firstIdx[ord(s[i]) - ord('a')] == len(s)):
                firstIdx[ord(s[i]) - ord('a')]  = i
            
        minIdx = len(s)
        for j in range(len(currCounts)):
            if(currCounts[j] == 1):
                minIdx = min(minIdx, firstIdx[j])
        
        if(minIdx != len(s)):
            return minIdx
        return -1