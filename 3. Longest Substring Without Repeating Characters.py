class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = []
        current_length = 0
        max_length = 0
        for idx in range(len(s)):
            letter = s[idx]
            if letter not in current_substring:
                current_substring.append(letter)
                current_length += 1
                if current_length >= max_length:
                    max_length = current_length
            else:  # letter in current_substring
                old_length = current_length  # Store the length of current_substring before modifying
                old_index = current_substring.index(letter)
                current_substring = current_substring[old_index + 1 :]
                current_substring.append(letter)
                current_length = (
                    current_length - old_index
                )  # Remove the first old_index + 1 elements, then append 1 elements

        return max_length
