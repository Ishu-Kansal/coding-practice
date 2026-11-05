class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda item: item[0])
        arrows = 0

        def isOverlap(first, second):
            if(first[1] >= second[0]):
                return True
            return False

        i = 0
        while(i < len(points)):
            currInterval = points[i]
            j = i + 1
            while(j < len(points) and isOverlap(currInterval, points[j])):
                currInterval = [currInterval[0], min(currInterval[1], points[j][1])]
                j += 1
            i = j
            arrows += 1
        

        return arrows
