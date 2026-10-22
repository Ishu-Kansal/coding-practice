class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalTime = customers[0][1]
        currTime = customers[0][0] + customers[0][1] # assume customer 1 has been served
        for i in range(1, len(customers)):
            arrival, wait = customers[i]
            print('curr time', currTime)
            thisWait = wait
            if(arrival < currTime): # arrived before last order was done
                thisWait += currTime - arrival
            
            currTime = max(currTime + wait, arrival + wait)
            totalTime += thisWait
        
        return totalTime / len(customers)