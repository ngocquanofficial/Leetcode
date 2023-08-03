class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.convert(s)
        first_index = 0
        last_index = len(s) - 1
        while last_index >= first_index:
            if s[last_index] == s[first_index]:
                first_index += 1
                last_index -= 1
            else:
                return False
        return True

    def convert(self, input_string):
        # Convert the string to lowercase
        lowercase_string = input_string.lower()

        # Remove all non-alphanumeric characters
        alphanumeric_string = "".join(
            char for char in lowercase_string if char.isalnum()
        )

        return alphanumeric_string
