class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i =="("or i =="{"or i =="[":
                stack.append(i)
            else:
                if i==")" and stack[-1]=="(":
                    stack.pop()
                elif i=="}" and stack[-1]=="{":
                    stack.pop()
                elif i=="]" and stack[-1]=="[":
                    stack.pop()
        if stack==[]:
            return True
        else:
            return False