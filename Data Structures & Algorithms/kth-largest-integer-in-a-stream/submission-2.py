import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Transform the list into a valid Min-Heap (runs in O(N) time)
        heapq.heapify(self.heap) 
        
        # 2. Throw away the smallest elements until we only have k left
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
    def add(self, val: int) -> int:
            # Case 1: The heap isn't full yet. Just add the number.
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, val)
                
            # Case 2: The heap is full. Only add the number if it's bigger than our current smallest VIP.
            elif val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
                
            # The top of the heap is always the kth largest
            return self.heap[0]
