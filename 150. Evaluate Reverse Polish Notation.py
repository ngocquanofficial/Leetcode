
# class Solution:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiple(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         return int(a / b)

#     def evalRPN(self, tokens):
#         operator = {
#             "+": self.add,
#             "-": self.subtract,
#             "*": self.multiple,
#             "/": self.divide,
#         }
#         stack = []
#         for token in tokens:
#             if token not in operator:
#                 stack.append(int(token))
#                 continue

#             # Here token is a operator
#             second_num = stack[-1]
#             stack.pop()
#             first_num = stack[-1]
#             stack.pop()
#             ans = operator[token](first_num, second_num)
#             stack.append(ans)

#         return stack[0]










# UPDATE Pi Day 2024
import math
class Solution:
    def evalRPN(self, tokens) :

        def add(a, b) :
            return int(a) + int(b)
        
        def subtract(a, b) :
            return int(a) - int(b)
        
        def mul(a, b) :

            return int(a) * int(b)
        
        def divide(a, b) :
            if b == 0 :
                print("ERROR")
                return
            
            return math.trunc(int(a) / int(b))
        
        stack = []

        map_func = {"+": add, "-": subtract, "*": mul, "/": divide}

        for token in tokens :
            if token not in map_func :
                stack.append(token)
                continue

            # ELSE 
            # Then calculate, append to the end of stack
            second = stack.pop()
            first = stack.pop()

            ans = map_func[token](first, second)

            stack.append(str(ans))

        return int(stack[0])


            


        

    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))

            


        
