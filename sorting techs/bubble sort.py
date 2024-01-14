a=[46,22,34,9,13,52]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    print(a)
    