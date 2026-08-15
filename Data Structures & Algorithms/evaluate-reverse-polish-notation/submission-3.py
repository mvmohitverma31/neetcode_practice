class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(a+b)
            elif tokens[i]=="-":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(a-b)
            elif tokens[i]=="*":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(a*b)
            elif tokens[i]=="/":
                b=int(stack.pop())
                a=int(stack.pop())
                stack.append(a/b)
            else:
                stack.append(tokens[i])
        return int(stack[0])