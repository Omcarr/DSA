class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        empt={}
        for i,n in enumerate(nums):
            diff= target-n
            if diff in empt:
                return [empt[diff],i]
            empt[n]=i
