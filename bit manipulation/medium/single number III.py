class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor^=i
        m,n=0,0
        set_bit=1
        while not(xor & set_bit):
            print(xor & set_bit)
            set_bit*=2
        print(set_bit)

        for i in nums:
            if not(i & set_bit):
                m^=i
            else:
                n^=i
        return [m,n]

        