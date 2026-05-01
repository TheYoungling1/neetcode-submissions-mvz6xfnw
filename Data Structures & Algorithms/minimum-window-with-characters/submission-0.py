class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # the minimum substring will be at least the length of t

        # the maximum substring will be whole of s, if even that doesnt contain t, then return "" lol

        # we can increase a sliding window up until it contains t, the try shorten the window

        # as a substring is continuous


        left = 0
        right = 0
        
        # Replaced 'full_substring' with variables to track the best window
        min_window = ""
        min_len = float("inf")

        seen = {}
        t_freq = {}
        count = len(set(t))
        
        # constructing hashmap for o(1) - [Kept exactly as you wrote it]
        for i in range(0, len(t)):
            if t[i] not in t_freq:
                t_freq[t[i]] = 0
            t_freq[t[i]] += 1

        # main right pointer moving loop
        while right < len(s):
            
            # [Kept exactly as you wrote it]
            if s[right] not in seen:
                seen[s[right]] = 0
            seen[s[right]] += 1

            # FIX 1: Change '>=' to '==' so we don't over-decrement the count
            if s[right] in t_freq and seen[s[right]] == t_freq[s[right]]:
                count -= 1
            
            # FIX 2: Bring the shortening loop INSIDE the main loop. 
            # We trigger this whenever count hits 0 (meaning the window is valid).
            while count == 0:
                
                # Check if this valid window is the smallest we've seen so far
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_window = s[left:right + 1]

                # Shortening logic (similar to your old code, but we don't return immediately)
                if s[left] in t_freq and seen[s[left]] - 1 < t_freq[s[left]]:
                    count += 1  # Breaking the window means we need that unique char again
                
                seen[s[left]] -= 1
                left += 1

            right += 1

        # If min_len is still infinity, we never found a window, so return ""
        return min_window
    
            
        

            
            