def canConstruct(ransomNote: str, magazine: str) -> bool:
    temp={} #'aa' 'aab'
    temp2={}
    for i in range(0,len(magazine)):
        temp[magazine[i]]=1+temp.get(magazine[i],0)
    
    for i in range(0,len(ransomNote)):
       temp2[ransomNote[i]]=1+temp2.get(ransomNote[i],0)

    return temp2<=temp
# from collections import Counter    
# def canConstruct(ransomNote: str, magazine: str) -> bool:
#         c1 = Counter(ransomNote)
#         c2 = Counter(magazine)
#         return c1 <= c2,type(c1)
print(canConstruct('aab','aancdb'))