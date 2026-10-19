class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while(i <= j):
            if(s[i] != s[j]):
                firstI = i
                firstJ = j
                isValid = True
                firstI += 1
                while(firstI <= firstJ):
                    if(s[firstI] != s[firstJ]):
                        isValid = False
                        break
                    firstI += 1
                    firstJ -= 1
                if(isValid):
                    return True

                firstI = i
                firstJ = j
                firstJ -= 1
                while(firstI <= firstJ):
                    if(s[firstI] != s[firstJ]):
                        return False
                    firstI += 1
                    firstJ -= 1
        
            i += 1
            j -= 1
        return True

