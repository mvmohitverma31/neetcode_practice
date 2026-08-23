class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        heap = []
        ans = []
        cooldown = deque()
        time = 0

        # Frequency map
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Max heap using negative frequency
        for task in freq:
            heapq.heappush(heap, (-freq[task], task))

        while heap or cooldown:

            # We have an available task
            if heap:
                x = heapq.heappop(heap)

                ans.append(x[1])
                time += 1

                # Task still has remaining occurrences
                if x[0] < -1:
                    cooldown.append((time + n, x[0] + 1, x[1]))

            # No available task, but something is cooling
            elif cooldown:

                # Jump directly to when the next task becomes available
                if cooldown[0][0] > time:
                    idle = cooldown[0][0] - time
                    ans.extend(["idle"] * idle)
                    time = cooldown[0][0]

                # Now release every task whose cooldown is over
                while cooldown and cooldown[0][0] <= time:
                    z = cooldown.popleft()
                    heapq.heappush(heap, (z[1], z[2]))


        return len(ans)