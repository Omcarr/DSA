class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        else:
            if nums[0]>nums[1]:
                return 0
            if nums[-1]>nums[-2]:
                return len(nums)-1
        i=len(nums)//2
        while i<len(nums)-1 and i>0:
            l=i-1
            r=i+1
            #print(nums[l],nums[0],nums[r])
            if nums[i]>nums[l] and nums[i]>nums[r]:
                return i
            elif nums[i]>nums[l]:
                i=r
            else:
                i=l
        

        