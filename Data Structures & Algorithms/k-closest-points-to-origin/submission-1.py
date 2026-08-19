class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for i in range(len(points)):
            n=points[i][0]**2+points[i][1]**2
            store=(-n,points[i])
            if len(heap)<k:
                heapq.heappush(heap,store)       
            else:
                if -store[0]<-heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,store)
        for i in range(k):
            ans.append(heap[i][-1])
        return ans