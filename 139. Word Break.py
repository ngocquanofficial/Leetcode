class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # Change wordDict to dictionary to have 0(1) time for finding
        word_dict = dict()
        min_len = len(wordDict[0])
        max_len = len(wordDict[0])
        for element in wordDict:
            part_len = len(element)
            word_dict[element] = None
            if min_len > part_len:
                min_len = part_len
            elif max_len < part_len:
                max_len = part_len

        for i in range(len(s) - 1, -1, -1):
            for idx in range(min_len, max_len + 1):
                if i + idx > len(s):
                    break
                if dp[i] == True:
                    break

                if s[i : i + idx] in word_dict:
                    dp[i] = dp[i + idx]
        return dp[0]
        # Each element in word_dict range from min_len to max_len length


wordDict = ["aaaa", "aaa"]
s = "aaaaaaa"
obj = Solution()
print(obj.wordBreak(s, wordDict))
