class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        print(nums)
        closest=float('inf')
        res=0
        i,k=0,len(nums)-1
        while i<len(nums)-2:
            j=i+1
            while j<k:
                ans=nums[i]+nums[j]+nums[k]
                if ans==target:
                    return target
                elif ans>target:
                    k-=1
                else:
                    j+=1
                diff=abs(target-ans)
                if diff<closest:
                    res=ans
                    closest=diff
            i+=1
            k=len(nums)-1
        return res