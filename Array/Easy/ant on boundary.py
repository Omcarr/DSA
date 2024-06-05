class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        res=0
        temp=0
        for i in nums:
            temp+=i
            if temp==0:
                res+=1
        
        return res
        