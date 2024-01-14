#my solution
def twoSum(nums:list[int], target: int) -> list[int]:
    mid=(len(nums))//2
    if nums[mid]>=target:
        start=0
        end=mid
    elif nums[-1]<target:
       start=0
       end=len(nums)-1
    else:
        start=mid
        end=len(nums)-1
    
    l,r=start,end
    while l<r:
        print(nums[l],nums[r],l,r)
        if nums[l]+nums[r]==target:
            return [l+1,r+1]
        elif nums[l]+nums[r]>target:
            r-=1
        else:
            l+=1

#optimal
class Solution:
 def twoSum(self,nums:list[int], target: int) -> list[int]:
    l,r=0,len(nums)-1
    while l<=r:
        sum=nums[l]+nums[r]
        if sum<target:
            l+=1
        elif sum>target:
            r-=1
        if sum==target:
            return[l+1,r+1]
    return []
    

    
print(twoSum([3,24,50,79,88,150,345],200))
print(7//2)