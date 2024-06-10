class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            s=l=0
            res=len(nums)+1
            for r,n in enumerate(nums):
                s+=n
                while s>=target:
                    s-=nums[l]
                    res=min(res,r-l+1)
                    l+=1
            if res==len(nums)+1:
                return 0
            return res        
        