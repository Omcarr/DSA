
def leaders(A, N):
        l=[]
        temp=0
        for i in range(N-2,-1,-1):
          if A[i]>temp:
               l.append(A[i])
               temp=A[i]
        l=[l[i] for i in range(len(l)-1, -1, -1)]
        l.append(A[-1])
        return l

print(leaders([16 ,17, 4, 3, 5, 2],6))
