class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res,l=0,0
        temp=1
        for  r in range(len(nums)):
            temp*=nums[r]
            while l<=r and temp>=k:
                temp//=nums[l]
                l+=1
            res+=(r-l+1)
        return res
    


            