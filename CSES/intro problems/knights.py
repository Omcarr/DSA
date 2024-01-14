m=int(input())

for n in range(1,m+1):
    moves=pow(n,2)*(pow(n,2)-1)//2 
#total ways n^2(n^2-1)/2 for nxn board
    knights_attack=4*(n-1)*(n-2)  
#only attacks at n+-1 and n+-2 positions so 8 cases possible 
#out of which are not on the board and half are repeated
    legal_moves=moves-knights_attack
    print(legal_moves)