class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        
        freqL = []

        for key, val in freq.items():
            freqL.append([key, val])
        
        freqL = sorted(freqL, key=lambda item: item[1], reverse=True)

        numPresses = {}
        available = 8
        currRound = 1

        for i in range(len(freqL)):
            letter, count = freqL[i]
            if(available == 0):
                available = 8
                currRound += 1
            numPresses[letter] = currRound
            available -= 1
        total = 0
        for ch in word:
            total += numPresses[ch]

        return total
