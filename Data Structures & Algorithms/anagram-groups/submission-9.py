class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def anagramString(strIn: str):
            counts = [0] * 26
            for ch in strIn:
                counts[ord(ch) - ord('a')] += 1
            ret = tuple(counts)
            
            return ret
    
        exists = {}

        for anagram in strs:
            converted = anagramString(anagram)
            if(converted in exists):
                exists[converted].append(anagram)
            else:
                exists[converted] = [anagram]
        
        resArr = []
        for key, val in exists.items():
            resArr.append(val)
        
        return resArr