class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=max(nums)
        res=cnt=l=0
        for r in range(len(nums)):
            if nums[r]==n:
                cnt+=1
            while cnt>=k:
                if nums[l]==n:
                    cnt-=1
                l+=1
            res+=l
        return res