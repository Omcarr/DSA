class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=0
        while l<r:
            h=min(nums[l],nums[r])
            area=h*(r-l)
            if area>res:
                res=area
            
            if nums[l]>nums[r]:
                r-=1
            else:
                l+=1
        return res