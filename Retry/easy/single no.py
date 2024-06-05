#------------------BIT MANIUPLUTION NEEDED-------------------
#sol accepted
class Solution:
 def singleNumber(self,nums: list[int]) -> int:
    emp = {}
    for n in range(0, len(nums)):
        emp[nums[n]] = 1+emp.get(nums[n], 0)
    for n in range(0, len(nums)):
     if emp[nums[n]]==1:
        return nums[n]
    return 0