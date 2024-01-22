def longestSubarray(nums: list[int]) -> int:
    cnt,res=0,0
    # if len(nums)==1:
    #     return 0
    # if 0 not in nums:
    #     return len(nums)-1
    
    l,r=0,1
    zero_cnt=0
    while r<len(nums):
        if nums[l]==1:
            if zero_cnt!=2:
                if nums[r]==0:
                    zero_cnt+=1
                    cnt-=1
                    if zero_cnt==1:
                        loc=r
                cnt+=1
                print(r,cnt)
                r+=1
            else:
                zero_cnt=0
                l=loc+1
                res=max(cnt,res)
        elif r==len(nums)-1:
             res=max(cnt,res)
        else:
            l+=1
    return res
            

print(longestSubarray(nums =[0,1,1,1,0,1,1,1]))