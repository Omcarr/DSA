class Solution:
  def kidsWithCandies(self,candies:list[int], extraCandies: int): #-> list[bool]:
    max_candies=0
    ans=[]
    for i in range(0,len(candies)):
        max_candies=max(max_candies,candies[i])
        
    for i in range(0,len(candies)):
     if candies[i]+extraCandies>=max_candies:
         ans.append(True)
     else:
           ans.append(False)
    return ans
    