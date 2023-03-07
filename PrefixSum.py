def prefix_sum(nums) :
    n = len(nums)
    if n == 1 :
        return nums
    if n == 2 :
        return [nums[0], nums[0]+nums[1]]
    mid = n // 2
    first = prefix_sum(nums[:mid+1])
    first_sum = sum(nums[:mid+1])
    second = [x + first_sum for x in prefix_sum(nums[mid+1:])]
    return first + second
    
    

nums = [1,1,1,1,1]
print(prefix_sum(nums))
        