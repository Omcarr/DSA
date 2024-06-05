#Sol works but brute forced 
def countBits(n: int) -> list[int]:
    binary_list=[]
    count1=[]
    i=0
    while i<=n:
        tc=0
        temp=bin(i)[2:]
        for j in range(0,len(temp)):
            if temp[j]=='1':
                tc+=1
            else:
                tc+=0
        count1.append(tc)
        binary_list.append(temp)
        i+=1
    
    return count1

print(countBits(5))
