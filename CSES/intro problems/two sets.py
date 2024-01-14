n=int(input())
val=n
step=0
set1,set2=[],[]
while val>0:
    if step%2==0:
      set1.append(val)
      set2.append(val-1)
      val-=3
    else:
      set1.append(val)
      set2.append(val+1)
      val-=1
    step+=1
    
if n%2!=0:
   set2.append(1)

if sum(set1)!=sum(set2) or len(set2)+len(set1)!=n:
   print('NO')

else:
   print('YES')
   print(len(set1))
   print(*set1,end=' ')
   print('')
   print(len(set2))
   print(*set2,end=' ')
   

          
