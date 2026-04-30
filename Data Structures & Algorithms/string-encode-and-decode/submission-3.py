class Solution:

    def encode(self, strs: List[str]) -> str:
       # find a way put a list into a string,
       # then have an algo to decompose the string back into a list
       # but then we have to allow for all possible ascii character 


        # hello, /world
        # hello//world
        # 
        
        final = ""
        for word in strs:
            n = len(word)
            final += str(n) + '#' + word
        print(final)
        return final
        
    def decode(self, s: str) -> List[str]:
        final = []
        while len(s) > 0:
            i = 0
            while s[i] != "#":
                i += 1
            
            num = int(s[0:i])
            # print(num)
            tmp = s[i:]
            # print("temp: " + tmp)
            word = tmp[1:num + 1]
            # print("word: " + word)
            s = tmp[num+1:]
            # print("s: " + s)
            final.append(word)
        
        return final
        
        
            

         