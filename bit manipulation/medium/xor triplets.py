class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)-1): # i cant be on the last position
            a=nums[i]
            for k in range(i+1,len(nums)): #k is always equal or greater than j
                a^=nums[k]
                #at any position if a=0, k-i possible combinations of partitions can be made
                if a==0:
                    res+=k-i
        return res

            