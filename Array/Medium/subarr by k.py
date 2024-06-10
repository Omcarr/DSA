from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        remainders=defaultdict(int)
        remainders[0]=1
        temp=0
        for n in nums:
            temp+=n
            r=temp%k
            res+=remainders[r]
            remainders[r]+=1

        return res
        