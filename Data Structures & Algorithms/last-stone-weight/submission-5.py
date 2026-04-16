import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # init array
        # while len(array) > 1:
        #   sort the array
        #.   take [0] and [1]
        #    replace the current arr etc...

        # n * n * log(n)

        # maintain a heap of some sort

        # take the top element 2 times, then repush to the heap

        # O(n), taking head would be O(1) and re-push would be /O(logn) (not sure), so overall itss O(n logn)


        # 1. Negate all values to simulate a Max-Heap
        max_heap = [-stone for stone in stones]
        
        # 2. Use standard Min-Heap heapify
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # 3. Pop the two "smallest" (most negative) elements
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            # 4. If they aren't equal, push the difference. 
            # Note: Because they are negative, first is technically smaller than second.
            # E.g., first = -10, second = -8. The smash leaves a 2 stone.
            # (-10) - (-8) = -2. This perfectly keeps the new weight negative!
            if first != second:
                heapq.heappush(max_heap, first - second)

        # 5. Return the positive value of the last stone, or 0 if empty
        if len(max_heap) == 1:
            return -max_heap[0]
        
        return 0