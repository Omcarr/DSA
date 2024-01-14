n=int(input())
apples=list(map(int,input().split()))
apples=sorted(apples)

b1,b2=[],[]
l,r=0,len(apples)-1
while r>l:
    b1.append(apples[l])
    b2.append(apples[r])
    l+=1
    r-=1
print(b2,b1)
diff=sum(b2)-sum(b1)
    
    


print(diff)