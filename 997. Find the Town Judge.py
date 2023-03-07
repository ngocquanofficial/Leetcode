class Solution:
    def findJudge(self, n, trust):
        if n ==1 and trust == [] :
            return 1
        first = [x[0] for x in trust]
        second = [y[-1] for y in trust]
        # get unique value
        first = list(set(first))
        second = list(set(second))
        total = list(range(1, n+1))
        ans = [x for x in total if x in second and x not in first]
        if len(ans) == 0 :
            return -1
        for people in ans :
            trusted = [i[0] for i in trust if i[-1] == people]
            if len(trusted) == n-1 :
                return people
        return -1