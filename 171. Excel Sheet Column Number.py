class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0
        for multi_ele in range(n - 1, -1, -1):
            ans += 26**multi_ele * (
                ord(columnTitle[n - 1 - multi_ele]) - ord("A") + 1
            )
        # multi_ele = [i for i in range(n-1, -1, -1)]
        # values = [ord(i) - ord("A") + 1 for i in columnTitle]

        # return sum([26**x * y for x, y in zip(multi_ele, values)])
        return ans
