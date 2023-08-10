class Solution:
    def countQuadruplets(self, nums):
        # Runtime-Memory trade-off using hash table
        # a + b + c = d means a + b = d - c, so
        # we store all d - c values in a hash table, then check for each a + b
        abstract = dict()
        ans = 0
        for c in range(2, len(nums) - 1):  # Due to a < b < c < d
            for d in range(c + 1, len(nums)):
                minus = nums[d] - nums[c]
                if minus not in abstract:
                    abstract[minus] = [[c, d]]
                else:
                    abstract[minus].append([c, d])

        # Then check for each sum a + b
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                current_sum = nums[a] + nums[b]
                if current_sum not in abstract:
                    # Can not find any (a,b,c,d) satisfy
                    continue

                for element in abstract[current_sum]:
                    if element[0] > b:  # Due to b < c
                        ans += 1
        return ans
