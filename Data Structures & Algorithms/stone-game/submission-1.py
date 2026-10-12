class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        counts = [0, 0] # [alice, bob]
        i = 0
        j = len(piles)-1
        turn = 0
        while(i <= j):
            # pick the pile with smallest cfr: my pick - revealed for opp
            if(i - j == 0):
                counts[turn % 2] += piles[i]
                i += 1
                continue
            
            cfrI = piles[i] - piles[i + 1]
            cfrJ = piles[j] - piles[j-1]
            if(cfrI > cfrJ):
                counts[turn % 2] += piles[i]
                i += 1
            else:
                counts[turn % 2] += piles[j]
                j -= 1
            turn += 1


        return counts[0] > counts[1]