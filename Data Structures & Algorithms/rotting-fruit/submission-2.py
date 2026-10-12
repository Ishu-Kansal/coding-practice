class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        minute = 0
        healthy = 0
        

        n = len(grid)
        m = len(grid[0])

        def inBounds(a, b):
            if(a >= 0 and a < n and b >= 0 and b < m):
                return grid[a][b]
            return -1

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 2):
                    rotten.append([i, j])
                    grid[i][j] = 0
                elif(grid[i][j] == 1):
                    healthy += 1
        
        if(healthy == 0):
            return 0
        
        while(len(rotten) > 0):
            toAdd = set()
            minute += 1
            while(len(rotten) > 0):
                r, c = rotten.popleft()
                print('exploring', r, c)
                if((r-1, c) not in toAdd and inBounds(r-1, c) == 1):
                    grid[r-1][c] = 2
                    toAdd.add((r-1, c))
                    healthy -= 1
                if( (r+1, c) not in toAdd and inBounds(r+1, c) == 1):
                    grid[r+1][c] = 2
                    toAdd.add((r+1, c))
                    healthy -= 1
                if((r, c-1) not in toAdd and inBounds(r, c-1) == 1):
                    grid[r][c-1] = 2
                    toAdd.add((r, c-1))
                    healthy -= 1
                if((r, c+1) not in toAdd and inBounds(r, c+1) == 1):
                    grid[r][c+1] = 2
                    toAdd.add((r, c+1))
                    healthy -= 1
                grid[r][c] = 0
            
            for key in toAdd:
                toList = list(key)
                rotten.append(toList)
        print('healthy', healthy)
        if(healthy == 0):
            return minute - 1
        return -1
                
            
            

