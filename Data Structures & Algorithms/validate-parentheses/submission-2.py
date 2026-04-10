class Solution:
    def isValid(self, s: str) -> bool:

        # for the first half, put letters in a stack

        # and for the second half, pop from the stack, and check if matches
        # the chars in the second haldf

        stack = deque()

        if len(s) % 2 != 0:
            return False

        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }


        #for every letter:
        # if the char is a start, add to the stack

        # if the char is not a start, then pop the stack to compare 

        for char in s:
            print(char)
            if char in "({[":
                stack.append(char)
                print(stack)
            else:
                print(stack.pop)
                if not stack or char != bracket_map[stack.pop()]:
                    return False

        if not stack: 
            return True
        
        return False

