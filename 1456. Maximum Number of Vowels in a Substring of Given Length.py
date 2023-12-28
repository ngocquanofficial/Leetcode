class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_first_substring = 0
        max_vowel = 0
        vowel = ("a", "e", "i", "o", "u")

        # First check the first k element:
        for i in range(0, k) :
            if s[i] in vowel :
                vowel_first_substring += 1
        max_vowel = vowel_first_substring

        current_vowel = vowel_first_substring
        if k == len(s) :
            return max_vowel

        for idx in range(k, len(s)) :
            add_term = 0
            if s[idx] in vowel :
                add_term += 1
            if s[idx-k] in vowel :
                add_term -= 1
            
            current_vowel += add_term
            if current_vowel > max_vowel :
                max_vowel = current_vowel
        
        return max_vowel

        
        
obj = Solution()
print(obj.maxVowels("tryhard", 4))