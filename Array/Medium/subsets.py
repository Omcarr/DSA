class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return 
            #decision to add
            subset.append(nums[i])
            dfs(i+1,subset)
            #decision to not add
            subset.pop()
            dfs(i+1,subset)
            return res
        return dfs(0,[])
            