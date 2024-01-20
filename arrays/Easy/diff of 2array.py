def findDifference(nums1: list[int], nums2: list[int]) ->list[list[int]]:
        c1={}
        c2={}
        res=[[],[]]
        for i in range(len(nums1)):
            c1[nums1[i]]=1+c1.get(nums1[i],0)
        for i in range(len(nums2)):
            c2[nums2[i]]=1+c2.get(nums2[i],0)
        
        for key in c1.keys():
             if key not in c2.keys():
                  res[0].append(key)

        for key in c2.keys():
             if key not in c1.keys():
                  res[1].append(key)
        
        return res

print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))