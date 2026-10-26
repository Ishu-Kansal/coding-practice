class Solution:
    def trap(self, height: List[int]) -> int:
        rightMax = [height[0]]
        leftMax = [height[len(height) - 1]]

        for i in range(1, len(height)):
            j = len(height) - i - 1
            rightMax.append(max(rightMax[i-1], height[i-1]))
            leftMax.append(max(leftMax[i-1], height[j + 1]))
        leftMax.reverse()
        
        waterCount = 0
        for i in range(len(height)):
            waterCount += max(min(leftMax[i], rightMax[i]) - height[i], 0)
        

        return waterCount

            
