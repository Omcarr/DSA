
            if i in ops:
                 a=stack.pop()
                 b=stack.pop()
                 stack.append(ans(i,a,b))
            else:
                 stack.append(int