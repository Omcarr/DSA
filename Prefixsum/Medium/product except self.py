def productExceptSelf(nums: list[int]) -> list[int]:
    pre=[1]
    for i in range(1,len(nums)):
        pre.append(pre[i-1]*nums[i-1])

    post=nums.copy()
    post[-1]=1
    for i in range(len(nums)-2,-1,-1):
        post[i]=nums[i+1]*post[i+1]
    
    res=[]
    for i in range(len(pre)):
        res.append(pre[i]*post[i])
    
    return res

print(productExceptSelf([4,3,2,1,2]))