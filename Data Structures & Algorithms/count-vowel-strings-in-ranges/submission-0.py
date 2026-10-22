class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSums = [0]
        
        def vowelStr(wordIn):
            vowels = set(['a', 'e', 'i', 'o', 'u'])
            if(wordIn[0] in vowels and wordIn[-1] in vowels):
                return True
            return False

        for word in words:
            if(vowelStr(word)):
                prefixSums.append(prefixSums[-1] + 1)
            else:
                prefixSums.append(prefixSums[-1])

        queryRes = []

        for query in queries:
            li = query[0]
            ri = query[1]
            queryRes.append(prefixSums[ri + 1] - prefixSums[li])
        return queryRes