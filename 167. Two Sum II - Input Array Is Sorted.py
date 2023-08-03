class Solution:
    def twoSum(self, numbers, target):
        first = 0
        last = len(numbers) - 1
        # Idea: Check by 2 pointers, if sum not satisfy then move
        while first < last:
            if numbers[first] + numbers[last] == target:
                # Due to the test has exactly 1 solution
                break
            elif numbers[first] + numbers[last] > target:
                last -= 1  # last become smaller
            else:
                first += 1
        output = [first + 1, last + 1]
        return output


print("!!!")
obj = Solution()
print(obj.twoSum([1, 2, 3], 2))
