class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        move=0
        while len(matrix)!=0 and len(matrix[0])!=0:

            if move%4==0: #first row turn left
                res+=matrix.pop(0)

            if move%4==1:#last coloumn go top to down
                for i in range(len(matrix)):
                    res.append(matrix[i].pop())

            if move%4==2:#last row go right to left
                res+=matrix.pop()[::-1]

            if move%4==3: #first coloumn go bottom to top
                for i in range(len(matrix))[::-1]:
                    res.append(matrix[i].pop(0))

            move +=1
        return res