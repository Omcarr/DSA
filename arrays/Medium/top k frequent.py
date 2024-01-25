#approach 1
class Solution:
  def topKFrequent(self,nums: list[int], k: int) -> list[int]:
    count={}
    l1={}
    l2=[]
    if k==len(nums):
        return nums
    for i in range(0,len(nums)):
       count[nums[i]] = 1 + count.get(nums[i], 0)

    for (key,value) in count.items():
        l1[value]=key
  
    temp=sorted(l1)

    i=-1
    while k>0:
        l2.append(l1[temp[i]])
        i-=1
        k-=1
    return l2


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count={}
    l2=[]

    for i in range(0,len(nums)):
       count[nums[i]] = 1 + count.get(nums[i], 0)

    while k>0:
     maxval,maxkey=0,0
     for (key,value) in count.items():
         if value>maxval:
            maxval=value
            maxkey=key
     del count[maxkey]
     l2.append(maxkey)
     k-=1
    return l2

#most optimal NEETCODE

# def topKFrequent(nums: list[int], k: int) -> list[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#         print(freq)
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
#         print(freq)
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res



#heap solution 25 jan
import heapq
def topKFrequent(nums: list[int], k: int) -> list[int]:
        res={}
        for i in range(len(nums)):
            res[nums[i]]=1+res.get(nums[i],0)
        pairs=[]
        for n,c in res.items():
            pairs.append([-c,n])
        ans=[]
        heapq.heapify(pairs)
        for _ in range(k):
            l=heapq.heappop(pairs)
            ans.append(l[1])
        return ans

print(topKFrequent([1,1,1,2,2,3],2))

