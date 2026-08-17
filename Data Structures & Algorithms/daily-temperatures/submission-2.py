class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        day=[]
        maxx=0
        maxxy=[]
        for i in range(len(temp)):
            if stack==[]:
                stack.append(temp[i])
                maxxy.append(i)
                day=len(temp)*[0]
            else:
                if len(stack)<=1:
                    if temp[i]>stack[-1]:
                        stack.pop()
                        day[maxxy[-1]]=i-maxxy[-1]
                        maxxy.pop()
                        maxxy.append(i)
                        stack.append(temp[i])
                    else:
                        stack.append(temp[i])
                        maxxy.append(i)
                else:
                    if temp[i]<=stack[-1]:
                        stack.append(temp[i])
                        maxxy.append(i)
                    else:
                        while stack!=[] and temp[i]>stack[-1] :
                            stack.pop()
                            day[maxxy[-1]]=i-maxxy[-1]
                            maxxy.pop()
                        stack.append(temp[i])
                        maxxy.append(i)
        return day