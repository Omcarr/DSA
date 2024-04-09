
def count_rearrangements(arr):
    MOD = 1000000007
    arr.sort()
    peak=arr[-1]
    left=0
    right=0
    for i in arr:
        if i<peak:
            left+=1
        elif i>peak:
            right+=1
    
    res=left*right*(len(arr)-1)
    


T = int(input())


for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_rearrangements(arr))
