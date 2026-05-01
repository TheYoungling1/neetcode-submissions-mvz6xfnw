class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # within each window, check iteratively the max within each window

        # observation, iss that since each window differ by 1 number, it will be dumb to re-compare fgor each window
        # we need a compare based off the old window

        # we can have a heap that we maintain that has the "head" be the max value at that window
        # then for a new window, we do 2 x O(logn) to remove the outgoing one, and add the curr one


        # but deleting a node not head is O(n log n), too expensive
        
        heap = []  # stores (-value, index)
        result = []
        
        for right in range(len(nums)):
            # Add current element
            # get the max on top, maintain the index
            heapq.heappush(heap, (-nums[right], right))
            
            # Once we've seen at least k elements, start recording maxes
            if right >= k - 1:
                left = right - k + 1
                
                # Lazy deletion: pop stale elements from the top
                while heap[0][1] < left:
                    heapq.heappop(heap)

                # head of heap, and its value, not its index
                result.append(-heap[0][0])
        
        return result
                
            



