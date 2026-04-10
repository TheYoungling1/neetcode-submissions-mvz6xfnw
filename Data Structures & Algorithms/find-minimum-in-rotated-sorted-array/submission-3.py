class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the smallest element is always afetr the largesr element

        # O(log n) indicates binary search, but binary searc requies the rray to be sorted, but sorting takes O(n logn) we have to find a way to
        # re-sort the array given to find the array in ascending order

        # Binary search how many times to rotate our current array

        # if the middle element is smaller than the head? then all the elements after it might be bigger than the middle and smaller than the head

        # so we shift len - middle times

        
        # if the middle element is bigger, than more the left pointer

        # arr = deque([1, 2, 3, 4, 5])
        # arr.rotate(2)  # Right rotate by 2
        # print(list(arr))  # [4, 5, 1, 2, 3]

        # left = 0
        # n = len(nums) - 1
        # right = n

        # while left <= right:
        #     mid = (right + left) // 2
        #     print(mid)

        #     if nums[mid] < nums[left]:
        #         arr = deque(nums)
        #         arr.rotate(n - mid + 1)
        #         nums = list(arr)
        #         left = left + (n - mid)
        #     else:
        #         left = mid + 1
            
        #     print(nums)
        
        # return nums[0]

        # lets let left keep track of the end of one section, and right to keep track of another


        left = 0
        n = len(nums) - 1
        right = n

        while left < right: # Notice we use < instead of <= to avoid infinite loops
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum must be to the right of mid
                left = mid + 1
            else:
                # Minimum could be mid or to the left
                right = mid

        return nums[left]                