class Solution(object):
    def removeElement(self, nums, val):
     nums[:]=[i for i in nums if i!=val]
     return len(nums)
    # # nums[:]=[x for x in nums if x!=val]
    # while val in nums:
    #     nums.remove(val)   
    # return len(nums)