class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = set()
        longest = -1
        i = 0
        while(i < len(s)):
            j = len(s)-1
            if(s[i] not in seen):
                seen.add(s[i])
                while( j > i and s[j] != s[i]):
                    j -= 1
                if(j == i):
                    j -= 1
                longest = max(longest, j - i - 1)
            i += 1
        return longest