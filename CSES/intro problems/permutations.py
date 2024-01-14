n=int(input())

if n==2 or n==3:
    print('NO SOLUTION')
elif n==4:
    print('2 4 1 3')
else:
    for i in range(n,0,-2):
        print(i,end=' ')
    for i in range(n-1,0,-2):
        print(i,end=' ')









