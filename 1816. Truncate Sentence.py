class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        last_space = -1
        ans = []
        number = 0
        for i in range(len(s)):
            if s[i] != " ":
                continue

            # When s[i] == ' '
            number += 1
            ans.append(s[last_space + 1 : i])
            last_space = i
            if number == k:
                break
        # Base case
        if number < k:
            ans.append(s[last_space + 1 :])

        return " ".join(ans)


s = "chopper is not a tanuki"
k = 5
obj = Solution()
print(obj.truncateSentence(s, k))
