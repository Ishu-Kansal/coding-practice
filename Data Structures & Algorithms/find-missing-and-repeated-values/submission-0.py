class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = -1 
        b = -1
        total = 0
        found = set()
        n = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] in found):
                    a = grid[i][j]
                found.add(grid[i][j])
                total += grid[i][j]
        
        b = int(a + ((n * n * (n*n + 1)) / 2 ) - total)
        return [a, b]