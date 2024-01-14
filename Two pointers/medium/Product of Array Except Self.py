#o(n2)needs to  be optimised
def product(nums: list[int]) -> list[int]:
    l,p=0,1
    res=[]
    while l<len(nums):
      for i in range(0,len(nums)):
        if l==i:
            pass
        else:
            p*=nums[i]
      l+=1
      res.append(p)
      p=1
    return res

def productExceptSelf(nums: list[int]) -> list[int]:
   res=[1]*len(nums)
   #computing and using all prefixes
   for i in range(1,len(nums)): #starting at index 1 as postion 0 has no  prefix
      res[i]=res[i-1]*nums[i-1]
   postfix=1
   #computing the postfix sum
   for i in range(len(nums)-1,-1,-1):
      res[i]*=postfix
      postfix*=nums[i]
   return res
      

print(productExceptSelf([5,6,7,8]))
