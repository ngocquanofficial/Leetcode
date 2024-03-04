class Solution1:
    def isPalindrome(self, x):
        if x < 0:
            return False

        origin = x
        reverse = 0
        # Now we create the reverse number of x
        while x != 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return origin == reverse

### 27.2.2024

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        max_len = 0
        current_len = 0

        for letter in s :
            if letter in window :
                current_len = 1
                window = set()
                window.add(letter)
                continue
            
            #ELSE
            current_len += 1
            window.add(letter)
            if current_len > max_len :
                max_len = current_len

        return max_len
        
s = "aab"

obj = Solution()
print(obj.lengthOfLongestSubstring(s))