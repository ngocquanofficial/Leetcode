class Solution:
    def shuffle(self, nums, n):
        first = nums[:n]
        second = nums[n:]
        output = []
        for i in range(n) :
            output.append(first[i])
            output.append(second[i])
        return output
