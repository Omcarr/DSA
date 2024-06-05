class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a,d=0,len(nums)-1
        nums.sort()
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=i+1
                l=j-1
                while k<l:
                    temp=nums[i]+nums[j]+nums[k]+nums[l]
                    if temp==target:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif temp>target:
                        l-=1
                    else:
                        k+=1
        return list(res)