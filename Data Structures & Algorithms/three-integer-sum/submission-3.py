class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find 3 nums that adds to 0

        # we also want to return distinct triplet
        # so [-1, -1, 2] = [2, -1, -1]

        # if none, then return []

        # we can break the question down to, give a num i
        # find 2 other nums in the list who sums to -i

        # we can use a 2 sum helper function, and run 2 sum for every num in nums

        # O(n^2)

        
        # else, we can sort it

        # [-4, -1, -1, 0, 1, 2]

        # have a pointer from i + 1 and the other pointer from end of string
        # target is -(nums[i]), and if the sum is currently smaller, move 
        # the left pointer right, and if sum is currently bigger, move the 
        # right pointer left

        # make pointer's skip the duplicated items when moving
        

        # O(n * n )


        nums = sorted(nums)

        print(nums)
        n = len(nums)

        total = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = n - 1
            target = 0 - nums[i]

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    total.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
            
        return total

