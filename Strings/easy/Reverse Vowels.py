#attempt 1
# def reverseVowels(s: str) -> str:
#     vowels=['a','e','i', 'o','u']
#     print(s)
#     emp=[]
#     for i in range(0,len(s)):
#         if s[i] in vowels:
#             emp.append(i)
#     print(emp)
#     s=list(s)
#     if len(emp)%2==0:
#        a=int(len(emp)/2)
#     else:
#      a=int((len(emp)-1)/2)

#     for i in emp[:a]:
#      temp=s[i]
#      s[i]=s[emp[-(i+1)]]
#      s[emp[-(i+1)]]=temp
#      print(i,s[i],s[emp[-(i+1)]])

#     s=''.join(i for i in s)
#     return s,emp

#my sol
def reverseVowels(s: str) -> str:
    vowels=['a','e','i', 'o','u','A','E','I','O','U']
    print(s)
    emp=[]
    for i in range(0,len(s)):
        if s[i] in vowels:
            emp.append(i)
    print(emp)
    if len(emp)%2==0:
       a=int(len(emp)/2)
    else:
     a=int((len(emp)-1)/2)
    s=list(s)
    for i in range(0,a):
       temp=s[emp[i]]
       s[emp[i]]=s[emp[-(i+1)]]
       s[emp[-(i+1)]]=temp
       print(s[emp[-(i+1)]],s[emp[i]])
    s=''.join(i for i in s)
    return s


#better sol
def reverseVowels(s: str) -> str:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels=set('AEIOUaeiou')

        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s