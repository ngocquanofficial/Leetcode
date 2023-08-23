from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transform = dict()  # Create transform from s to t
        unique = dict()
        ans = []
        if len(s) != len(t):
            return False
        n = len(s)  # = len(t) also

        for i in range(n):
            if s[i] not in transform:
                transform[s[i]] = t[i]
                if t[i] in unique:
                    return False
                unique[t[i]] = None
            # If transform[s[i]] exists
            if t[i] != transform[s[i]]:
                return False

        for i in range(n):
            ans.append(transform[s[i]])
        ans_string = "".join(ans)
        print(ans_string)

        return ans_string == t


obj = Solution()
print(obj.isIsomorphic("badc", "bada"))
