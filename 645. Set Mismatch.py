class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        ans1 = []
        ans2 = []
        my_dict = dict()
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        for i in range(1, n + 1):
            if i not in my_dict:
                ans2.append(i)
                continue

            # Where i in my_dict
            if my_dict[i] == 2:
                ans1.append(i)

        return ans1 + ans2
