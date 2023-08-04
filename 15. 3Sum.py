class Solution:
    def threeSum(self, nums):
        # Base case:
        if len(nums) < 3:
            return []

        # time_appear store the index of each value occur in nums
        time_appear = dict()

        for idx in range(len(nums)):
            if nums[idx] not in time_appear:
                time_appear[nums[idx]] = [idx]
            else:
                time_appear[nums[idx]].append(idx)

        ans = []  # ans will store the output result
        distinct_value = list(time_appear.keys())  # distinct value that appear in nums

        # Base case: Only zero in nums
        if len(distinct_value) == 0:
            # Then it must contain full of 0
            if set(nums) == 0:
                return [[0, 0, 0]]
            else:
                return []

        # Base case :
        if 0 in time_appear:
            if len(time_appear[0]) >= 3:
                ans.append([0, 0, 0])
        # Then, we remove the case [0,0,0] when consider the next case

        # The case i + i + j = 0
        for i in distinct_value:
            if -2 * i not in time_appear or i == 0:
                # i == 0 means the case [0,0,0] we do not consider
                continue
            # Here is the satisfy solution, which is -2i in distinct_value, then [i,i,-2i]
            i_indices = time_appear[i]
            if len(i_indices) >= 2:
                ans.append([i, i, -2 * i])

        # End of the case 2i + j = 0, if len(distinct_value) == 2, then the algorithms will stop
        if len(distinct_value) == 2:
            return ans

        # The case i, j, k are distinct
        distinct_value = sorted(distinct_value)
        for i in range(len(distinct_value) - 2):
            for j in range(i + 1, len(distinct_value) - 1):
                # Due to sorted list, it mean that distinct[i] < distinct[j]

                k_value = -(distinct_value[i] + distinct_value[j])
                if k_value not in time_appear:
                    continue
                if (
                    k_value == distinct_value[i] or k_value == distinct_value[j]
                ):  # We do not consider the previous case [i, i, j]
                    continue

                if distinct_value[j] < k_value:
                    # Here the distinct_value[i], distinct_value[j], k_value is a satisfy list
                    ans.append([distinct_value[i], distinct_value[j], k_value])

        return ans
