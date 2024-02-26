class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current_num = nums[0]
        for num in nums :
            if num == current_num :
                count += 1
                continue

            # ELSE
            count -= 1
            if count < 0 :
                current_num = num
                count = 1

        return current_num
            


        