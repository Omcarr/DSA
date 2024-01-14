#defining your own alnum() slows down the code
# def validch(c):
#     if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
#        return True
#     return False
def isPalindrome(s: str) -> bool:
    t=''.join([x for x in s if x.isalnum()]).lower()
    print(t)
    l=0
    r=len(t)-1
    while r>=(len(t)//2):
        if t[l]!=t[r]:
           return False
        l+=1
        r-=1
    return True

print(isPalindrome('"A man, a plan, a canal: Panama"'))