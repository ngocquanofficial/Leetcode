class Solution:
    def decodeMessage(self, key, message):
        base_ord = ord("a")
        current_ord = base_ord
        transform = dict()
        for letter in key:
            if letter == " ":
                continue
            if letter in transform:
                continue
            # Here letter not exist in transform
            transform[letter] = chr(current_ord)
            current_ord += 1

        ans_list = []
        for element in message:
            if element == " ":
                ans_list.append(" ")
                continue

            ans_list.append(transform[element])

        return "".join(ans_list)
