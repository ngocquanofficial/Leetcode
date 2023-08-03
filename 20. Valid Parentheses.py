class Solution:
    def isValid(self, s: str) -> bool:
        open_char = ["[", "(", "{"]
        close_char = ["]", ")", "}"]
        char_dict = {"[": "]", "(": ")", "{": "}"}
        stack = []  # List in python is a type of stack
        # Idea: The last open_char must match with corresponding next close_char
        # Then we put step by step each character into the stack, if we meet a close char,
        # it must match with the previous character, then we remove both of them
        for char in s:
            if char in open_char:
                stack.append(char)
            else:  # char in close
                if stack == []:  # The close char must appear after a open char
                    return False
                # it must match with the last open char
                if char_dict[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        # After insert and remove, stack for valid parenthesis must be empty.
        if stack == []:
            return True
        else:
            return False
