class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        A=set()
        for n in nums:
            if n in A:
                return True
            A.add(n)
        return False
