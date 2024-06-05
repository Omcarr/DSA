def equalPairs( grid: list[list[int]]) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                #print(grid[i],[grid[x][j] for x in range(len(grid))])
                if grid[i]==([grid[x][j] for x in range(len(grid))]):
                 res+=1
                #print(' ')
        return res 


print(equalPairs(grid=[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))