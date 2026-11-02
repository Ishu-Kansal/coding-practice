class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        for i in range(len(nums)):
            if(nums[i] in index):
                index[nums[i]].append(i)
            else:
                index[nums[i]] = [i]
        
        for num, indexArr in index.items():
            if(len(indexArr) >= 2):
                j = 1
                while(j < len(indexArr)):
                    if(indexArr[j] - indexArr[j-1] <= k):
                        return True
                    j += 1
        
        return False