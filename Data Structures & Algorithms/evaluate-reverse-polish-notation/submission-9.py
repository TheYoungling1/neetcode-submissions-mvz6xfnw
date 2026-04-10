import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # put the operators in a stack
        # + whatever the calculation is between the last operator 

        # everytime we see a number, we push it, then repush the operted output
        # back onto the stack

        stack = deque()

        # (1+2) * 3

        # first therm in the operation is always in the the initial state
        # we push the results back onto the stack, this doesnt interfere
        # with the arithematic order

        # (1+2) * (2+3)

        # ["1", "2", "+", "2", "3", "+", "*"]

        # hence, for this case, we only take the most rcent 2 numbers 

        result = tokens[0]
        for item in tokens:
            if item in "+-*/":
                number_2 = stack.pop()
                number_1 = stack.pop()
                match item:
                    case "-":
                        result = number_1 - number_2
                    case "+":
                        result = number_1 + number_2
                    case "*":
                        result = number_1 * number_2
                    case "/":
                        result = int(number_1 / number_2)

                stack.append(result)           
            else:
                stack.append(int(item))

        print(result)

        return int(result)
