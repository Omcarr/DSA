def findDuplicate(nums: list[int]) -> int:
        n=len(nums)-1
        sums=0
        for i in range(len(nums)):
            t=nums[i]
            sums^=t
        print(isinstance(n,int))
        return sums-n


print(findDuplicate([2,2,2,2,2]))