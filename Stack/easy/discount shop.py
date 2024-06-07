class Solution:
    def finalPrices(self, nums: List[int]) -> List[int]:
        l=0
        while l<len(nums)-1:
            r=l+1
            while r<len(nums):
                diff=nums[l]-nums[r]
                if diff>=0:
                    nums[l]=diff
                    break
                else:
                    r+=1
            l+=1
        return nums
            