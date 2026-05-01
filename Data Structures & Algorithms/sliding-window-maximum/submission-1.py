class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        result = []
        right = 0

        while right < len(nums):
            # add to the monotically increasing queue
            # we add in the index for better out of bound detection

            # so the head of the queue is max we've seen so far

            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            # see if we need to pop from left

            if right >= k - 1:
                left = right - k + 1
                
                while q[0] < left:
                    q.popleft()
                
                result.append(nums[q[0]])

            right += 1
        
        return result
