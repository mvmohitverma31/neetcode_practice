class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in tasks:
            freq[i] = freq.get(i, 0) + 1
            
        heap = []
        for i in freq:
            heapq.heappush(heap, (-freq[i], i))
            
        cooldown = deque()
        time = 0
        
        while heap or cooldown:
            # 1. Bring tasks back from cooldown if they are ready
            while cooldown and cooldown[0][0] <= time:
                z = cooldown.popleft()
                heapq.heappush(heap, (z[1], z[2]))
                
            # 2. Process available task or fast-forward time during idles
            if heap:
                x = heapq.heappop(heap)
                time += 1
                if x[0] + 1 < 0:
                    cooldown.append((time + n, x[0] + 1, x[1]))
            else:
                # Direct optimization: Jump directly to the next ready task's time
                time = cooldown[0][0]

        return time