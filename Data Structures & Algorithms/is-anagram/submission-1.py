class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a hashmap (dict)

        dict_s = {}
        dict_t = {}

        for num in s:
            if num not in dict_s:
                dict_s[num] = 1
            else:
                dict_s[num] += 1

        for num in t:
            if num not in dict_t:
                dict_t[num] = 1
            else:
                dict_t[num] += 1


        if dict_s == dict_t:
            return True
        else:
            return False