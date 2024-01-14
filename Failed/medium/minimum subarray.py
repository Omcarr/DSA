# def minSubArrayLen(target: int, nums: list[int]) -> int:
#     if target in nums:
#         return 1
#     slidelen=2
#     i=0
#     # [2,3,1,2,4,3]
#     while i<len(nums)-1:
#         if i+slidelen<=len(nums)-1:
#          subarr=nums[i:i+slidelen]
#          i+=1
#          if sum(subarr)==target:
#             return slidelen,subarr
#          else:
#           slidelen+=1
#          print('here')
    
#     return 0


def minSubArrayLen(target: int, nums: list[int]) -> int:
    if target in nums:
        return 1
    slidelen=2
    i=0
    # [2,3,1,2,4,3
      
    return 0
print(minSubArrayLen(6,[2,3,0,2,4,3]))

        
