class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # can only replace at most k characters
        # find the length of the lognest substring that contains only
        # k + 1 distinct characters

        left = 0
        max_length = 0

        # keep a dictionary of the frequency so far
        freq = {}
        max_freq = 0
        for right in range(0, len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # 2. Update the historical max frequency (the watermark)
            max_freq = max(max_freq, freq[s[right]])

            # 3. Check if the window is invalid
            window_length = right - left + 1
            while window_length - max_freq > k:
                # We must shrink/shift the window
                freq[s[left]] -= 1
                left += 1
                # Notice we do NOT recalculate max_freq here!
                window_length = right - left + 1


            max_length = max(max_length, right - left + 1)
        
        return max_length


            
            