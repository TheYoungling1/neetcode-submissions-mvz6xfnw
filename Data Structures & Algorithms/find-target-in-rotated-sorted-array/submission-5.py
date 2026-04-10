class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums) - 1
        right = n

        # [4, 5, 6, 7, 8, 1, 2] target 8
        # mid = 7, 7 > 4 and target > 4


        while left <= right:
            mid = (left + right) // 2
            
            # 1. Did we find the target?
            if nums[mid] == target:
                return mid
            
            # 2. Is the LEFT half perfectly sorted?
            if nums[left] <= nums[mid]:
                # Is the target securely sandwiched in this sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Dump to the right
            
            # 3. Otherwise, the RIGHT half MUST be perfectly sorted
            else:
                # Is the target securely sandwiched in this sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Dump to the left
                    
        # 4. Target is not in the array
        return -1