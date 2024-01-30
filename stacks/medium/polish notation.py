def evalRPN(tokens: list[str]) -> int:
        ops=['+','-','*','/'] 
        def ans(op,a,b):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            return int(a/b)
        
        stack=[]
        for i in tokens:
            if i in ops:
                 a=stack.pop()
                 b=stack.pop()
                 ans=int(int(f'{b}{i}{a}'))
                 stack.append(ans)
            else:
                 stack.append(int(i))
        return(stack[0])


print(evalRPN(tokens = ["4","13","5","/","+"]))