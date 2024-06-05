#write a code to check if a head is valid
#implement pop and push with min heap

#heap[0] is always a garbage value, heap[1] is the real root, we insert elements at heap[-1] always

#heah has two properties:
# 1)Structural property i.e. no holes till last level, values inserted left to right 
# and then logic to maintain the order property

# 2)ordered property i.e. maintain the min/max order according to the heap
#multiple values are allowed inside a heap. in case of min heap which child is greater doesnt matter for the parent

# formuale
# left child=2*i
# right child=2i+1
# parent=i//2

#always pop at heap[1] then that hole replace it with heap[-1]. now pucker down heap[-1] to its valid position

#time complexity for pop and push is O(logN) i.e. height of the heap tree as its balanced

#getting heap min/max o(1)

#can convert an array into a heap using .heapify() o(N)