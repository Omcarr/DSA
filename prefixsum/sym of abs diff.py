def getSumAbsoluteDifferences( nums: list[int]) -> list[int]:
    n=len(nums)-1
    pre=[0]*(n+1)
    post=nums.copy()
    post[-1]=0
    for i in range(1,len(nums)):
        pre[i]=pre[i-1]+nums[i-1]
    for i in range(n-1,-1,-1):
        post[i]=nums[i+1]+post[i+1]
    res=[]
    for i in range(len(nums)):
        res.append((nums[i]*(2*i-n))+post[i]-pre[i])

    return res

print(getSumAbsoluteDifferences(nums = [1,4,6,8,10]))