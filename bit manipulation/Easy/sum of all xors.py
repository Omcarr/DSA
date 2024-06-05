class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,res):
            if i==len(nums):
                return res
            return dfs(i+1,res^nums[i]) + dfs(i+1,res)
        return dfs(0,0)