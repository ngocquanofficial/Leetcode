class Solution:
    def makeFancyString(self, s: str) -> str:
        current = 1
        ans = s[0]
        for index, value in enumerate(s[1:]):
            index = index + 1  # due to loop from s[1:]
            if value != s[index - 1]:
                current = 1
                ans += value
                continue

            current += 1
            if current == 3:
                current -= 1
                continue
            else:
                ans += value

        return ans


obj = Solution()
s = "leeetcode"
print(obj.makeFancyString(s))
