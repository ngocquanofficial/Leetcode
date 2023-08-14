class Solution:
    def findKthLargest(self, nums, k):
        array = nums[:k]
        array.sort()
        current = array[0]
        if len(nums) == k:
            return current
        for i in range(k, len(nums)):
            # If nums[i] < current, it do not appear in largest k element array
            if nums[i] <= current:
                continue
            # ELSE
            # ensure that exactly k-element in the array
            array.pop(0)
            # Now array only has k-1 element
            # Move nums[i] to the correct index
            for idx in range(k - 1):
                if array[idx] >= nums[i]:
                    array.insert(idx, nums[i])
                    break
            else:
                # If not inserted, then nums[i] is the largest element
                array.append(nums[i])

            current = array[0]
        return array[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))
