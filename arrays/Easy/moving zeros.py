
def moveZeroes(nums: list[int]) -> None: 
#   for l in range(0,len(nums)):
#     for r in range(l,len(nums)-1):
#       if nums[l]==0:
#         nums[l],nums[r]=nums[r],nums[l]
  l=0
  r=1
  for r in range(0,len(nums)):
    if nums[l]==0 and nums[r]!=0:
      nums[l],nums[r]=nums[r],nums[l]
    if nums[l]!=0:
     l+=1
  print(nums,l,r)

moveZeroes([0,0,1,2,4,5,9,0])