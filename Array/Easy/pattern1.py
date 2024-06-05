# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end='')
#     print('')

# for i in range(0,5):
#     for j in range(i,5):
#         print("*",end='')
#     print('\n',end='')


# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j+1,end='')
#     print('\n',end='')

# for i in range(0,9):
#     if i<5:
#      for j in range(0,i+1):
#         print('*',end='')
#     else:
#      for k in range(i-4,5):
#         print('*',end='')
#     print('\n',end='')

for i in range(0,5):
     for j in range(0,5):
          if j>3-i:
               print('*',end='')
          else:
               print(' ',end='')
     for k in range(i,-1,-1):
          if k<4-i:
               print('*',end='')
          else:
               print(' ',end='')
     print('\n',end='')
     
               
    #  for k in range(i4,5):
    #     print('*',end='')
   
   