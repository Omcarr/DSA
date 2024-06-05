class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count=[0]*(len(nums)+1)
        for i in nums:
            idx=min(i,len(nums))
            count[idx]+=1  
        temp=0
        for i in range(len(nums),-1,-1):
            temp+=count[i]
            if temp==i:
                return i
        return -1   