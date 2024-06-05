def maxFrequency(nums: list[int], k: int) -> int:
    l,r=0,1
    ans=1
    while k>=0 and r<len(nums):
        if nums[r]-nums[l]<=k:
            ans+=1
        k-=nums[r]-nums[l]
        r+=1
        l+=1
     
    return ans
print(maxFrequency(nums = [3,9,6], k = 2))