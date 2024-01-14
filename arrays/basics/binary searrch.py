def search(nums: list[int], target: int) -> int:
    mid=(len(nums)//2)
    start,end=0,mid+1
    if target>nums[mid]:
        start,end=mid+1,len(nums)
    for val in range(start,end):
        if nums[val]==target:
            return val
    return -1
print(search([5],5))
   
