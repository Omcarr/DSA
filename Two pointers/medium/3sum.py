def threeSum( nums: list[int]) -> list[list[int]]:
        nums.sort()
        l,j,r=0,1,len(nums)-1
        ans=set()
        while j<r:
            s=nums[l]+nums[j]+nums[r]
            if s==0:
                ans.add((nums[l],nums[j],nums[r]))
                j+=1
            elif s>0:
                r-=1
            else:
                l+=1
    
            
        ans=[list(a) for a in ans]
        return ans
       
print(threeSum([0,0,0]))