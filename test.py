class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        time_appear = dict()
        # time_appear store the index of each value occur in nums
        for idx in range(len(nums)):
            if nums[idx] not in time_appear:
                time_appear[nums[idx]] = [idx]
            else:
                time_appear[nums[idx]].append(idx)
        print(time_appear)
        ans = []
        distinct_value = list(time_appear.keys())
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
                print("3!")
        # The case i + i + j = 0
        for i in distinct_value:
            if -2 * i not in time_appear or i == 0 :
                continue
            # Here is the satisfy solution
            i_indices = time_appear[i]
            j_indices = time_appear[-2 * i]
            if len(i_indices) >= 2:
                ans.append([i, i, -2 * i])
                print([i, i, -2 * i], "2!")
        # End of the case 2i + j = 0, if len(distinct_value) == 2, then the algorithms will stop
        if len(distinct_value) == 2:
            return ans
        # The case i, j, k are distinct
        for i in range(len(distinct_value) - 2):
            for j in range(i + 1, len(distinct_value) - 1):
                k_value = -(distinct_value[i] + distinct_value[j])
                if k_value not in time_appear:
                    continue
                if k_value == distinct_value[i] or k_value == distinct_value[j]:
                    continue

                # Here the distinct_value[i], distinct_value[j], k_value is a satisfy list
                ans.append([distinct_value[i], distinct_value[j], k_value])

        # Remove duplicate list, for example [1,2,3] and [1,3,2] is the same
        unique_lists = {}
        for inner_list in ans:
            frozen_set = frozenset(inner_list)
            if frozen_set not in unique_lists:
                unique_lists[frozen_set] = inner_list

        ans = list(unique_lists.values())

        return ans


nums = [-1, 0, 1, 0]
obj = Solution()
obj.threeSum(nums)
