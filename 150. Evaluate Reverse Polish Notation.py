class Solution:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiple(self, a, b):
        return a * b

    def divide(self, a, b):
        return int(a / b)

    def evalRPN(self, tokens):
        operator = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiple,
            "/": self.divide,
        }
        stack = []
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
                continue

            # Here token is a operator
            second_num = stack[-1]
            stack.pop()
            first_num = stack[-1]
            stack.pop()
            ans = operator[token](first_num, second_num)
            stack.append(ans)

        return stack[0]
