str1=input().upper()
str2=sorted(str1)
pali=len(str2)*[0]

count={}
for i in range(0,len(str1)):
    count[str1[i]]=1+count.get(str1[i],0)

l,r=0,len(str2)-1
#even frequency fron back of palindrome
for key in count.keys():
    if count[key]%2==0:
        while count[key]!=0:
            pali[l]=key
            pali[r]=key
            l+=1
            r-=1
            count[key]-=2

#odd frequency at middle
for key in count.keys():
    if count[key]%2!=0:  
        while count[key]!=0:
         pali[l]=key
         l+=1
         count[key]-=1

l,r=0,len(str2)-1
isPali=True
while r>l:
    if pali[l]!=pali[r]:
        isPali=False
        break
    l+=1
    r-=1
    
ans=''
if isPali:
    for k in pali:
        ans+=k
    print(ans)
else:
    print('NO SOLUTION')

