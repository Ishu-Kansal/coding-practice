class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [0] * (len(nums)+1)
        for i in range(len(counts)):
            counts[i] = set()
        countMap = {}
        counts[0] = set(nums)
        for num in nums:
            currCount = countMap.get(num, 0)
            counts[currCount].remove(num)
            counts[currCount + 1].add(num)
            countMap[num] = currCount + 1
        myList = []

        for i in range(len(counts)-1, -1, -1):
            if(len(counts[i]) > 0):
                for elem in counts[i]:
                    myList.append(elem)
            if(len(myList) >= k):
                return myList
        

      