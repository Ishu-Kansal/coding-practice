class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPtr = 0
        tPtr = 0

        while(tPtr < len(t) and sPtr < len(s)):
            if(t[tPtr] == s[sPtr]):
                sPtr += 1
                tPtr += 1
            else:
                sPtr += 1
        
        return len(t) - tPtr