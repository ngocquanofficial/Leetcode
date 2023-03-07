class Solution:
    def find(self, s, k) : # find first index of value k in s
        for i in range(len(s)) :
            if s[i] == k :
                return i
        return -1 # if k not in s
    def isSubsequence(self, s: str, t: str) -> bool:
        # Base case 
        if len(s) == 0 :
            return 'true'
        if len(t) == 0 : # and len(s) != 0
            return 'false'
        x = s[0]
        index = Solution.find(self, t, x)
        if index == -1 :
            return 'false'
        return Solution.isSubsequence(self, s[1:], t[index+1:])
    
solu = Solution()
s = "abc"
t = "ahbgdc"
print(Solution.isSubsequence(solu, s, t), s, t)