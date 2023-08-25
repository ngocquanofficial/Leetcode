class Solution:
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
