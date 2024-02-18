#leetcode 1481
class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        res={}
        for i in range(len(nums)):
            res[nums[i]]=1+res.get(nums[i],0)
        
        res=sorted(res.values())
        i=0
        while k and i<len(nums):
            if res[i]!=0:
                   res[i]-=1
                   k-=1
            else:
              i+=1
        ans=0
        for i in res:
            if i!=0:
                ans+=1
        return ans
       

