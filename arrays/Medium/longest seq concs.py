class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans=0
        nums=set(nums)
        for n in nums:
            if n-1 not in nums:
                start=1
                while (n+start) in nums:
                    start+=1
                ans=max(ans,start)
        return ans
