class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        i,k=0,len(nums)-1
        while i<len(nums)-2:
            j=i+1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif s>0:
                    k-=1
                else:
                    j+=1
            i+=1
            k=len(nums)-1
        return ans

