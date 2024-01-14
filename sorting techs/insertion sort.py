def insertionSort(a):
   for i in range(1,len(a)):
    #start from postion 1 to neglect one unnessary loop
    for j in range(i,0,-1):
        #reverse order swaping for each internal loop
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
 
# Driver code to test above
a = [12, 11, 13, 5, 6]
insertionSort(a)
for i in range(len(a)):
    print (a[i],end=' ')


