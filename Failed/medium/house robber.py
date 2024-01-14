def rob(nums: list[int]) -> int:
    sum_even,sum_odd=0,0
    for even in range(0,len(nums),2):
        sum_even+=nums[even]
    for odd in range(1,len(nums),2):
        sum_odd+=nums[odd]
    
    if len(nums)>2:
     sum1,sum2=nums[0],nums[1]
     for i in range(3,len(nums),2):
        sum1+=nums[i]
     for i in range(4,len(nums),2):
        sum2+=nums[i]
    else:
       sum1,sum2=0,0
    
    robbed=max(sum_even,sum_odd,sum1,sum2)
    return robbed

print(rob([1,2,1,0]))