#better solution, much concise, o(1), o(1)
def isValidSudoku1(board: list[list[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))


#beats 86%, o(1), o(1)
def isValidSudoku2(board: list[list[str]]) -> bool:
    r,c=0,0
    seen_row,seen_column=[],[]

    while r<9 and c<9:
        for i in range(0,9):
         #to validate row
         if board[r][i]!='.':
            if board[r][i] not in seen_row:
             seen_row.append(board[r][i])
            else:
             return False
            
         if board[i][c]!='.':
         #to validate coloumns
           if board[i][c] not in seen_column:
             seen_column.append(board[i][c])
           else:
             return False
        print(seen_column)
        seen_column,seen_row=[],[]  
        r+=1
        c+=1

    r,c,gap=0,0,0
    seen_3x3=[]
    reset_matrix=[3,6,9]
    while gap<7:
     for c in range(0+gap,3+gap):
       if board[r][c]!='.':
         if board[r][c] not in seen_3x3:
           seen_3x3.append(board[r][c])
         else:
           return False
     r+=1
     if r in reset_matrix:
       seen_3x3=[]
     if r==9:
       r=0
       gap+=3

    return True     

board =[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(isValidSudoku1(board))