class Solution:
    def checkString(self, s):
        first_b = -1
        last_a = -1
        status = False
        for i in range(len(s)):
            if s[i] == "a":
                continue

            first_b = i
            break
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "b":
                continue
            last_a = i
            break
        # Base case : there is not b in the array
        if first_b == -1:
            return False
        # If last_a < first_b, then return True
        if last_a < first_b:
            return True
        else:
            return False


obj = Solution()
s = "bbb"
print(obj.checkString(s))
