def singleNumber(nums: list[int]) -> int:
        
        res = nums[0]
        for i in range(1,len(nums)):
            res = res ^ nums[i]
            print(res)
        
        return res

print(singleNumber([4,1,2,1,2]))