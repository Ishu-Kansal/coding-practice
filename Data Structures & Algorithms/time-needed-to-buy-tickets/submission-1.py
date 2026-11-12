class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        total = 0
        numTickets = tickets[k]
        for i in range(k):
            total += min(numTickets, tickets[i])
        for i in range(k+1, len(tickets)):
            total += min(numTickets - 1, tickets[i])
        return total + numTickets