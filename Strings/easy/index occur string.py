def strStr(haystack: str, needle: str) -> int:
    r=0
    i=0
    # haystack = "sadbutsad", needle = "sad"
    while i<len(haystack):
        #  print(haystack[i],needle[r],i,r)
         if haystack[i]==needle[r]:
              r+=1
              i+=1
              if r==len(needle):
                return i-r
         else:
              #if needel matches fro some part but midway fails
              #we need to reset the haystack to haystack-needle+1 position
              i=i-r+1
              r=0  
            
    return -1
              
print(strStr('mississippi','issip'))


#most optimal
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        return_val = -1
        for i in range(haystack_len):
            check_str = haystack[i:needle_len+i]
            if  check_str == needle:
                return i

        return return_val
    

#python cheatcode
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) if needle in haystack else -1