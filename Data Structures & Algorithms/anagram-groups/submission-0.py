class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have a dicitonary of the different characters as 

        # for anagram words, where all the characters are the same but the order isnt
        # Sorting the word will make every word the same

        sorted_strs = []
        for word in strs:
            sorted_strs.append("".join(sorted(word)))

        #print(sorted_strs)

        # Find the indices of the words that are anagrams

        # use a dictionary that takes in the sorted words as key, and keep 
        # a list of the dicies of the same words
        
        counting = {}
        for i, s_word in enumerate(sorted_strs):
            if s_word not in counting:
                counting[s_word] = [] 
            counting[s_word].append(strs[i])
        
        print(counting)
    
        final_arr = []
        for anagram in counting:
            final_arr.append(counting[anagram])
        
        return final_arr

