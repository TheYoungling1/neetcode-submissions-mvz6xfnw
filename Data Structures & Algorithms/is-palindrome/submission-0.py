import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use regex to extract only alphanumeric characters and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        left_pt = 0
        right_pt = len(cleaned) - 1
        while left_pt < right_pt:
            print("left " + cleaned[left_pt])
            print("right " + cleaned[right_pt])
            if cleaned[left_pt] != cleaned[right_pt]:
                return False
            left_pt += 1
            right_pt -= 1
        return True