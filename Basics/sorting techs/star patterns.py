step='a'
def pat12():
 for i in range(0,4):
    for j in range(0,i+1):
        print(step+j,end='')
    for k in range(6,2*i,-1):
        print(' ',end='')
    for m in range(i+1,0,-1):
        print(step+m-1,end='')
    print('')
    
# for i in range(0,5):
#     for j in range(0,i+1):
#        print(step,end=' ')
#        step+=1
#     print('')

original_string = "a"
character_b = original_string[1]

print(character_b)




# for i in range(0,5):
#     for j in range(0,i+1):
#         print(1,end=' ')
#     print('')



