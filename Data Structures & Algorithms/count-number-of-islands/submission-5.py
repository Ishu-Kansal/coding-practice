class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [
            [1, 0], [0, 1], [-1, 0], [0, -1]
        ]

        def inBounds(row, col):
            if(row >= 0 and row < ROWS and col >= 0 and col < COLS):
                return True
            return False

        def dfs(r, c):
            nonlocal count
            stack = []
            if(grid[r][c] == '1'):
                stack.append([r, c]) 
                count += 1
            while(len(stack) > 0):
                i, j = stack.pop()
                grid[i][j] = '0'
                for direction in DIRECTIONS:
                    currI, currJ = i + direction[0], j + direction[1]
                    if(inBounds(currI, currJ) and grid[currI][currJ] == '1'):
                        stack.append([currI, currJ])
                        grid[currI][currJ] = '0'
            
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j)
        
        return count
                    
