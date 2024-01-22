#Brute force
# word='BANANA'
# vowels=['A', 'E', 'I', 'O', 'U']
# all_words,kev_words,stu_words=[],[],[]

# for i in range(len(word)):
#     for j in range(0,len(word)):
#      if word[i:j+1]!='':
#       all_words.append(word[i:j+1])

# for word in all_words:
#     if word[0] in vowels:
#        kev_words.append(word)
#     else:
#        stu_words.append(word)

# if len(stu_words)<len(kev_words):
#    print(f'Kevin {len(kev_words)}')
# else:
#    print(f'Stuart {len(stu_words)}')

   
#optimal solution
word='BANAASA'
vowels=['A', 'E', 'I', 'O', 'U']
k,s=0,0
for i in range(len(word)):
    if word[i] in vowels:
        k+=len(word)-i
    else:
        s+=len(word)-i
if s<k:
   print(f'Kevin {k}')
elif k>s:
   print(f'Stuart {s}')
else:
    print('Draw')