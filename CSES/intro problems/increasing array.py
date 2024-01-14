n=int(input())
vals=list(map(int, input().split()))
moves=0
for i in range(0,n-1):
    if vals[i]>vals[i+1]:
        moves+=(vals[i]-vals[i+1])
        vals[i+1]=vals[i]
        
print(moves)