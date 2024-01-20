def mergeAlternately(word1: str, word2: str) -> str:
        l=len(word1)
        r=len(word2)
        ls=min(l,r)
        rs=""
        for i in range(0,ls):
            rs+=word1[i]
            rs+=word2[i]
        
        if word1[ls:]:
            rs+=word1[ls:]
            
        if word2[ls:]:
            rs+=word2[ls:]
        
        
        return rs

print(mergeAlternately(word1='ab',word2='pqrs'))