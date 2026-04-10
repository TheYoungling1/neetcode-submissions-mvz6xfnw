class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if there is one unique, check with sliding windows of 1
        # if there are two unique, check with sliding windows of 2 etc...

        # def variable_window(s):
        #     left = 0
        #     max_length = 0
        #     state = {} # Could be a hash map, set, or integer to track the window's state
            
        #     for right in range(len(s)):
        #         # 1. Add s[right] to the window's state
        #         # ...
                
        #         # 2. Check if the window is invalid. If so, shrink from the left.
        #         while invalid_condition(state):
        #             # Remove s[left] from the window's state
        #             # ...
        #             left += 1
                    
        #         # 3. Update the optimal answer (max length, min length, etc.)
        #         max_length = max(max_length, right - left + 1)
                
        #     return max_length

        left = 0
        max_length = 0
        window = deque()


        # The while invalid_condition: loop ensures we do the absolute bare minimum amount 
        #of shrinking required to make the window valid again. Once it's valid, we immediately
        # stop shrinking and go back to expanding the right side to see if we can beat our high score.
        for right in range(0, len(s)):
            window.append(s[right])

            while len(set(window)) != len(window):
                window.popleft()

            max_length = max(max_length, len(window))

        return max_length