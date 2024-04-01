### UPDATE 1.4.2024: Using Binary Search Idea
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def partial(min, max) :
            if min > max :
                return -1
            if min == max : 
                if nums[min] == target :
                    return min
                else :
                    return -1

            mid = (max - min) // 2 + min

            if nums[mid] == target :
                return mid
            
            if nums[mid] > target :
                return partial(min, mid - 1)

            if nums[mid] < target :
                return partial(mid + 1, max)
        
        return partial(0, len(nums) - 1)
        







class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        # Base case nums has only 1 element
        if len(nums) == 0:
            if nums[0] == target:
                return 0
            else:
                return -1
        while end > start + 1:  # Avoid base case: end = start + 1, then mid = start
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:  # nums[mid] < target
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        

### UPDATE
