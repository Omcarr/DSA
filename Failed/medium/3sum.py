def threeSum(nums: list[int]) -> list[list[int]]:
    entry=0
    res={}
    while entry<len(nums)-2:
        for i in range(entry+1,len(nums)-1):
            for j in range(i+1,len(nums)):
             #print([nums[entry],nums[i],nums[j]])
             sum=nums[entry]+nums[i]+nums[j]
             if sum==0 and (nums[entry],nums[i],nums[j] not in res):
                res.update([nums[entry],nums[i],nums[j]])
        entry+=1
    print(res)


print(threeSum([-1,0,1,2,-1,-4]))