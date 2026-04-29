class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force, would be O(n^2)

        # this problem is depends on finding the smallest element of each sub-list

        # and see if the current smallest is bigger than the current element 
        # we are on, in which case, we will add it to the curr list, as all 
        # future elements in the sublist will be bigger than this element 
        

        # actually, we should probably think of the problem this way if the
        # current element is bigger than the max subsequence num so far, then add 

        # if curr is smaller than the rest of the substring seen soo far, then 
        # add to the start of the subsequence

        # and dp[i] can represent the smallest num seen from i to len(nums)

        # If you're standing at index i, what does it mean to ask: "What's the longest increasing subsequence that starts at index i?" (Call this LIS(i).)
        # Suppose you knew LIS(j) for every j > i. How would you compute LIS(i)? Specifically: which j's are "eligible" to come after i in an increasing subsequence? 

        # see if we can add to the min


        memo = {}
        def recurse(i):
            if i in memo:
                return memo[i]

            max_length = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length = recurse(j)
                    max_length = max(length, max_length)
            
            # max length is the best subsequence lence we can do for i + 1
            # returns 0 if to subsequence from i + 1 to len(nums) is bigger than i
            memo[i] = 1 + max_length
            # LIS(i) and the +1: answers "if I'm forced to use nums[i] as the start, what's the best I can do?"
            return memo[i]
        
        # cycles for all possible starting?
        return max(recurse(i) for i in range(len(nums)))


        