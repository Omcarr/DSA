class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res=0
        b=[]
        for i in range(len(grid)):
            c=[]
            for x in range(len(grid)):
              c.append(grid[x][i])
            b.append(c)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i]==(b[j]):
                 res+=1
        return res 

   
                
                    
        