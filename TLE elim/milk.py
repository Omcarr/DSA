n=int(input())
while n:
    n-=1
    X, Y, Z = map(int, input().split())
    if Y*Z<=X:
        print('Mazze')
    else:
        print('Dudh Mehenga Hai')