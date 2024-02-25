class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]]
        res += [pref[i]^pref[i+1] for i in range(len(pref)-1)]
        return(res)
        