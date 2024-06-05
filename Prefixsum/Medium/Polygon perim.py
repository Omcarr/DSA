class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        #<--------Prefix Sum and SORT------------------>
        #nums.sort()
        # prefix_sum=[nums[0]]*len(nums)
        # for i in range(1,len(nums)):
        #     prefix_sum[i]=prefix_sum[i-1]+nums[i]

        # r=len(nums)-1
        # while r>=2:
        #     if nums[r]<prefix_sum[r-1]:
        #         return prefix_sum[r]
        #     r-=1
        # return -1

        #More of a Pythonic solution
        while len(nums)>=3:
            p=max(nums)
            nums.remove(p)
            if p>=sum(nums):
                continue
            else:
                return p+sum(nums)
        return -1




