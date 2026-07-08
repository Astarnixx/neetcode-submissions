from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid):
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxarea,area=0,0
        def bfs(r,c): #To visit neighbours of a 1, find its island, and mark in grid
            nonlocal area
            q = deque()
            grid[r][c] = 0 #Mark the cell as visited
            q.append((r,c)) #Append the cell coordinates to the queue
            while q:
                row,col = q.popleft()
                area+=1
                for dr,dc in directions: #Check all 4 directions, if the neighbour is a 1, mark it as visited and add to queue
                    nr,nc = row+dr,col+dc
                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0 #Mark the neighbour cell as visited
        for r in range(ROWS): #Visit each cell, if it is a 1 find its island and increment no. of islands by 1
            for c in range(COLS):
                if grid[r][c]==1:
                    bfs(r,c)
                    maxarea = max(maxarea,area)
                    area=0
        return maxarea