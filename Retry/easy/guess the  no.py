#---------------NOT COMPLETED----------------------------

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import random
class Solution():
 def guess(num: int) -> int:
     return 

 def guessNumber(self,n: int) -> int:
    start,end=1,n
    while start<=end:
     mid=end//2
     result=self.guess(mid)
     if result==0:
        return mid
     elif result==1:
        start=mid+1
     elif result==-1:
        end=mid-1
    return -1


mid=(1+10)//2
print(mid)