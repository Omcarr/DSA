class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        res += [pref[i]^pref[i+1] for i in range(len(pref)-1)]
        return(res)
        


#can do a better sol using bit maniup?

