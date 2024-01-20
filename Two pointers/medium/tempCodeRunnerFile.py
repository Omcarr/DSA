
            if nums[l]+nums[r]==k:
                ops+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1