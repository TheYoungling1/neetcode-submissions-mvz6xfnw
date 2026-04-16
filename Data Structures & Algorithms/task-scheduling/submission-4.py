class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # for each identical task, we want there to be a gap of at least "n" in index
        # important: all tasks have the same cooldown, so no cases where its the most optimal to place at the end just because its cooldown is the least

        # simply add n empty element between every element in the array
        # O(n), but not correct solution

        # since we have to wait at least n times before executing thew same task, is there a way to execute another seperate. task during this time

        # at each time, we want to add the available task that has the least takss left? greedy?

        
        # we can have an array of counters for when the task can next be executed
        # {"X": n, "Y": n}

        # and at runtime, we check the task with most frequency still left whose counter is < 0
        # then put it in the arr, and reset the counter

        # O(n^2) how will we know whats the task to execute at runtime

        # make if we make the counter into a heap, and just execute whatever task that can be executed then?
        

        # have 2 datas tructures

        # a heap, which determines what to get executed at runtime, this will be oprgniased by the frequency of the task
        # this uses a greedy approach, because as all task cooldowns are, the onees with most frequency will be a min cap

        # at each loop, pop the head, and if that task has mroe frequencies, add it into a queue to wait until its cooldown finishes
        # and as a queue is first in first out, and we are only popping one task at the time, 

        # Because every task has the exact same cooldown duration ($n$), the first task to enter the waiting room is guaranteed to
        # be the first one to leave it. The queue naturally stays sorted by the ready_time. You only ever need to check the front of it.

        
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        max_heap = []
        for count in task_freq.values():
            # Use negative counts to simulate a max-heap in Python
            heapq.heappush(max_heap, -count)

        cooldown = deque() # Stores pairs of [remaining_freq, absolute_ready_time]
        counter = 0

        # Loop continues as long as we have tasks waiting to run OR currently on cooldown
        while max_heap or cooldown:
            counter += 1

            # 1. Check if the task at the front of the queue is done cooling down
            if cooldown and cooldown[0][1] == counter:
                ready_task_freq = cooldown.popleft()[0]
                heapq.heappush(max_heap, ready_task_freq)

            # 2. Execute the most frequent available task from the heap
            if max_heap:
                current_freq = heapq.heappop(max_heap)
                current_freq += 1 # Adding 1 to a negative number brings it closer to 0
                
                if current_freq < 0:
                    # Append with the absolute time it will be ready to run again
                    absolute_ready_time = counter + n + 1
                    cooldown.append([current_freq, absolute_ready_time])

        return counter


        

