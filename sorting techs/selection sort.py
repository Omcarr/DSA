a=[46,22,34,9,13,52]
for i in range(0,len(a)):
    mini=a[i]
    val=i
    for j in range(i+1,len(a)):
     if a[j]<mini:
        mini=a[j]
        val=j
    a[i],a[val]=mini,a[i]
    print(a)