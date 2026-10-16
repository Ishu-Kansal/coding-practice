class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestToRight = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = greatestToRight
            greatestToRight = max(temp, greatestToRight)
        
        return arr
