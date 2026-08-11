class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dec=True
        for i in s:
            if i =="("or i =="{"or i =="[":
                stack.append(i)
            else:
                if stack!=[]:
                    if i==")" and stack[-1]=="(":
                        stack.pop()
                    elif i=="}" and stack[-1]=="{":
                        stack.pop()
                    elif i=="]" and stack[-1]=="[":
                        stack.pop()
                    else:
                        dec=False
                else:
                    dec=False
        if stack==[] and dec==True:
            return dec
        else:
            dec=False
            return dec