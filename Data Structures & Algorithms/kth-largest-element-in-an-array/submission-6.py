class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting takes O(n*logn) -> very bad if the number of nums is very large, but k is smalllll


        # we want a way to store and process k nodes dynamically

        # min-heap of size k

        # where the root of the heap is the "smallest of the k-heap" i.e. the kth largest

        heap = []


        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]