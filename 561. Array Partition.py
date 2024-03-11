class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_num = sorted(nums)
        
        return sum(sorted_num[0: len(nums) : 2])
    
# PROVE:
# 2n number (a1,b1),...,(an, bn), such that ai <= bi
# So maximize sum(ai) means minimize sum (bi-ai) due to sum of 2n nums is constant, then
# 2 sum(ai) = sum (ai + ai) = sum (ai + bi - (bi - ai) ) = const - sum(bi -ai)
# Then we can prove that the optimal sum is as code above