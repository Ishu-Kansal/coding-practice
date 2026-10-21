class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        longest = 0
        while(right < len(s)):
            currChar = s[right]
            if(currChar in seen):
                while(left < right and currChar in seen):
                    seen.remove(s[left])
                    left += 1
            seen.add(currChar)
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest