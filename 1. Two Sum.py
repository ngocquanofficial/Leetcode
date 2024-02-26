# class Solution:
#     def twoSum(self, nums, target) :
#         dict_nums = {}
#         for i in range(len(nums)) :
#             dict_nums[nums[i]] = i
#         for i in range(len(nums)):
#             if target - nums[i] in dict_nums :
#                 j = dict_nums[target - nums[i]]
#                 if i != j :
#                     return [i, j]



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)

        first_ind = -1

        second_ind = -1

        for i, num in enumerate(nums) :
            if target - num in set_nums :

                first_ind = i

                second_num = target - num
                break
        print(first_ind)
        # The first num must be found befor the second num
        for i, num in enumerate(nums[first_ind+1 :]) :
            if num == second_num :
                second_ind = i
                return [first_ind, second_ind]

            












