
def majorityElement(nums: list[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
            print(candidate,count)
        
        return candidate

print(majorityElement([6,6,6,6,6,3,2,3,2]))