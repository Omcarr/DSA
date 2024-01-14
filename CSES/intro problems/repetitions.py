seq=input().upper()
l=0
r=1
count=1
while r<len(seq):
    if seq[l]==seq[r]:
        r+=1
        count=max(count,r-l)
    else:
     l=r
     r+=1

print(count)
    


    


