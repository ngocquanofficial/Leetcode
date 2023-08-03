class Solution:
    def searchMatrix(self, matrix, target):
        # First, we need to find what row target number belongs to
        first_list = [row[0] for row in matrix]
        first_row = 0
        last_row = len(first_list) - 1
        # We need to find maximun element in first_list that smaller or equal to target
        while last_row > first_row + 1:
            mid_row = (last_row + first_row) // 2
            if first_list[mid_row] == target:
                return True
            elif first_list[mid_row] > target:
                last_row = mid_row
            else:  # first_list[mid_row] < target
                first_row = mid_row

        # In here, last_row - first_row = 1,
        # first_list[first_row] <= target <= first_list[last_row]

        # return the maximun element in first_list that smaller or equal to target
        if first_list[last_row] <= target:
            target_row = last_row
        else:
            target_row = first_row

        array = matrix[target_row]
        # Here, continue binary search on 1D Array
        first = 0
        last = len(array) - 1
        while last > first + 1:
            mid = (last + first) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                last = mid
            else:
                first = mid

        if array[first] == target:
            return True
        elif array[last] == target:
            return True
        else:
            return False
