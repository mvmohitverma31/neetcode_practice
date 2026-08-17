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
                while stack!=[] and temp[i]>stack[-1] :
                    stack.pop()
                    day[maxxy[-1]]=i-maxxy[-1]
                    maxxy.pop()
                stack.append(temp[i])
                maxxy.append(i)
        return day