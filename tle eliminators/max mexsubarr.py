def find_mex(nums):
    sorted_nums=sorted(nums)
    mex=0
    res=0

    if sorted_nums[0]==0:
        for i in range(1,len(sorted_nums)-1):
            if sorted_nums[i+1]>sorted_nums[i]+1:
                   mex=sorted_nums[i]+1
        if mex==0:
            mex=max(nums)+1
    max_seen=False
    for i in nums:
        if i==max(nums):
            max_seen=True
        if i<mex:
            res+=1
        if max_seen:
            break
    return res

T=int(input())
for _ in range(T):
    N=int(input())
    nums_arr= list(map(int, input().split()))
    print(find_mex(nums_arr))

        