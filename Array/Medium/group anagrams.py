class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in range(len(strs)):
            key= str(sorted(strs[i]))
            if key not in res.keys():
                res[key]=[strs[i]]
            else:
                res[key].append(strs[i])
        ans=[]
        for value in res.values():
            ans.append(value)
        return ans
        