import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        words=sorted(words)
        res={}
        for i in range(len(words)):
            res[words[i]]=1+res.get(words[i],0)
        vals=[-x for x in res.values()]

        w=[]
        heapq.heapify(vals)
        for _ in range(k):
                if vals:
                    t=-heapq.heappop(vals)
                    for n,c in res.items():
                          if c==t and n not in w and len(w)<k:
                                w.append(n)
       
        return w
#print(topKFrequent(words =["i","love","leetcode","i","love","coding"], k = 2))