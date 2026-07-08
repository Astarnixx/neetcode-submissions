class Solution:
    def maxAreaOfIsland(self, grid):
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxarea = 0
        area = 0
        def dfs(r,c): #To visit neighbours of a 1, find its island, and mark in grid
            nonlocal area
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0:
                return 
            grid[r][c] = 0
            area += 1
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for r in range(ROWS): #Visit each cell, if it is a 1 find its island and increment no. of islands by 1
            for c in range(COLS):
                if grid[r][c]==1:
                    dfs(r,c)
                    maxarea = max(maxarea, area)
                    area = 0
        return maxarea