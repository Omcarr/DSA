#attempt 1,beats 61% time,20%memory
# def wordPattern(pattern: str, s: str) -> bool:
#     codes={}
#     s=s.split()

#     if len(set(pattern))!=len(set(s)) or len(pattern)!=len(s):
#        return False

#     i=0
#     for letter in pattern:
#         codes[letter]=s[i]
#         i+=1
#     i=0
#     for l in s:
#         if codes[pattern[i]] !=l:
#          return False
#         i+=1
#     return True

#beats 90%,42%
def wordPattern(pattern: str, s: str) -> bool:
    codes={}
    s=s.split()

    if len(set(pattern))!=len(set(s)):
        return False
    if len(pattern)!=len(s):
       return False

    for i in range(0,len(pattern)):
     if pattern[i] not in codes:
         codes[pattern[i]]=s[i]
     elif codes[pattern[i]]!=s[i]:
         return False

    return True
 
print(wordPattern('abba','dog cat cat dog'))
        