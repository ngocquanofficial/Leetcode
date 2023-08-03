class Solution:
    def peakIndexInMountainArray(self, arr):
        first = 0
        last = len(arr) - 1
        while last > first + 1:  # at least 1 element between last and first
            mid = (first + last) // 2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] > arr[mid + 1]:  # and array[mid] < array[mid - 1]
                last = mid
            else:
                first = mid
        # if there is not any return, then first or last is the peak

        if first == 0:
            return last
        elif last == len(arr) - 1:
            return first

        if arr[first] > arr[first + 1] and arr[first] > arr[first - 1]:
            return first
        else:
            return last
