class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    # check for a fixed sliding window of size len(s1)
    
        # shrinking windows, 
        s1_dict = {}
        for letter in s1:
            if letter not in s1_dict:
                s1_dict[letter] = 0
            
            s1_dict[letter] += 1
    
        print(s1_dict)
        

        window = {}
        for i, letter in enumerate(s2):
            if letter not in window:
                window[letter] = 0
            window[letter] += 1
            print(window)

            if i >= len(s1) - 1:
                old = s2[i - len(s1) + 1]
                if window == s1_dict:
                    return True
                if old in window:
                    if window[old] == 1:
                        del window[old]
                    else:
                        window[old] -= 1
                    

        return False