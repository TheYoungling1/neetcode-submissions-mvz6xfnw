class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # multiply all num in the array

        # For each i, divide the product by nums[i]

        # O(n)

        # Follow up: Don't use division operation

        # For each product in index i, its product without it 
        # is Prod(i-1) * Prod(i + 1)

        # Somehow store there 2 vars

        #key prod(i+1) = nums[i+1] * nums[i+2] *... nums[n] 
        # = nums[n] * ... nums[i+1] * nums[i+1]
        # This can be found in O(n) time in one loop

        forward = [0]*len(nums)
        forward[0] = nums[0]
        for i in range(0, len(nums) - 1):
            forward[i+1] = forward[i] * nums[i+1]

        backward = [0] * len(nums)
        backward[0] = nums[len(nums) - 1]

        # Build the running product from right to left
        # backward[1] will be nums[n-1] * nums[n-2], and so on
        for i in range(0, len(nums) - 1):
            # Use the previous product (i) to calculate the next one (i+1)
            backward[i + 1] = backward[i] * nums[len(nums) - 2 - i]
        print(forward)
        print(backward)

        #Prod(i-1) * Prod(i + 1)

        #prod(i+1) = backward[len(nums) - i - 1]
        prod = [0]*len(nums)
        prod[0] = backward[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            prod[i] = forward[i - 1] * backward[len(nums) - i -2]
        prod[len(nums) - 1] = forward[len(nums) - 2]
        return prod


        





        