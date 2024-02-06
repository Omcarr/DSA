class Stack():
    def __init__(self) -> None:
        self.items=[]
    
    def __str__(self):
        return f"{self.items}"
    
    def pop(self):
        if self.items:
           self.items=self.items[:-1]
        else:
            print('Error: Stack is empty')

    def append(self,n):
        self.items[len(self.items):]=[n]
    
   

stack_object=Stack()
stack_object.append(1)
print(stack_object)
stack_object.pop()
stack_object.pop()
print(stack_object)