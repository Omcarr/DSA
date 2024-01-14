#two pointer approcah
#----------------COULD NOT COME UP WITH A SOLUTION on own-----------------
# class Solution:
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
    last=m+n-1
    while m>0 and n>0:
        #check if last element of nums1 is greater than nums2 that
        if nums1[m-1]>nums2[n-1]:
            nums1[last]=nums1[m-1]
            m-=1
        #if not fill up nums2 last elemeent is last of nums1
        else:
            nums1[last]=nums2[n-1]
            n-=1
        last-=1
    #in case m runs out but n still has elemnts so directly place them at front of m
    while n>0:
        nums1[last]=nums2[n-1]
        n-=1
        last-=1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))


# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     # nums2=nums2[:n]
#     # temp=nums1[:m]
#     # nums1=[0]*(m+n)
#     # a,b=0,0
#     # range_1=max(m,n)
#     # for i in range(0,range_1*2,2):
#     #     if a<m:
#     #         nums1[i]=temp[a]
#     #         a+=1
#     #         print(nums1,i,a)
#     #     if b<n:
#     #         nums1[i]=nums2[b]
#     #         b+=1
#     #         print(nums1,i,b)

#      temp=nums1[:m]
#      nums1=[0]*(m+n)
#      nums2=nums2[:n]
#      j=1
#      for i in range(0,m):
#           nums1[i*2]=temp[i]
#      for i in range(0,n):
#           if j<n:
#            nums1[j]=nums2[i]
#            j+=2

#      return nums1

# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
#     looplen=m+n-2
#     p1=0
#     p2=0
#     temp=nums1
#     nums1=[]
#     print(nums1)
#     while looplen>=0:
#         if p1<m:
#          nums1.append(temp[p1])
#          p1+=1
#         if p2<n:
#          nums1.append(nums2[p2])
#          p2+=1
#         looplen-=1 
#     return nums1
# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
#     p1,p2,i=0,0,0
#     temp=nums1
#     nums1=[0]*(m+n)
#     for j in range(0,m+n-1):
#         if p1<m:
#             nums1[i]=temp[p1]
#             p1+=1
#             i+=1
#         if p2<n:
#             nums1[i]=nums2[p2]
#             p2+=1
#             i+=1
#     return sorted(nums1) 
# print(merge([1,2,3,0,0,0],3,[2,5,6],3))

#nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]

# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list:
#    nums1=nums1[0:m]
#    for i in range(0,n):
#       nums1.append(nums2[i])
#    nums1=sorted(nums1)


