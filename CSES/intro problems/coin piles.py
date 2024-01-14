n=int(input())
piles=[]
for i in range(0,n):
    coins=list(map(int,input().split()))
    piles.append(coins)
#piles are ready now
    
for case in piles:
    a,b=case[0],case[1]
    total=a+b
    can_empty_piles=False
    if total%3==0 and (2*min(a,b)>= max(a,b)):
    #mod 3 because each turn we will remove 3 coins. so total coins must be divisible by 3
    #we will keep removing 2 coins from the bigger stack
    #so the smaller stack must be atleast half the size of the bigger stack 
        can_empty_piles=True

    if can_empty_piles:
        print('YES')
    else:
        print('NO')