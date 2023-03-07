def pivotIndex( nums) :
    total_sum = sum(nums)
    n = len(nums)
    if total_sum - nums[0] == 0 : # special case when sum(nums[1:]) = 0
        return 0
    for i in range(1, n) :
        if 2 * sum(nums[:i]) + nums[i] == total_sum :
            return i
    return -1

import sys
def input() :
    x = [int(i) for i in sys.stdin.readlines().split()]
    return x
nums = [1,2,3,2,1]
print(pivotIndex(nums))