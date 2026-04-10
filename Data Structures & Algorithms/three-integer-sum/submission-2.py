class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use the 2 sum as another helper function

        # For each array in nums, find its correcting 2 sum for target - sum

        # 2 sum is O(n), so 3 sum is O(n^2)
        nums = sorted(nums)
        arr = []

        for i in range(0, len(nums) - 2):
            # Skip duplicate in outer loop
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # we already have i in the triplet, and the previous iterations
            # would have already considered i with elements prior to i
            left = i + 1
            # Last element
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]
                # 
                if sum < -nums[i]:
                    left += 1
                elif sum > -nums[i]:
                    right -= 1
                else:
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

        return arr

        