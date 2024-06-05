class Solution:
    def check(self, nums: List[int]) -> bool:
        

        n=len(nums)
        sort=sorted(nums)
        for i in range(n):
            newlist=nums[i:]+nums[:i]

            if newlist==sort:
                return True

        return False
        


        