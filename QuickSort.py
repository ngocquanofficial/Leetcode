# array = [int(i) for i in input().split()]


class QuickSort:
    def __init__(self, array):
        self.array = array

    def quick_sort(self, i, j):
        if i >= j:
            return
        pointer = self.partition(i, j)
        self.quick_sort(i, pointer - 1)
        self.quick_sort(pointer + 1, j)

    def sort(self):
        self.quick_sort(0, len(self.array) - 1)

    def partition(self, i, j):
        if i >= j:
            return
        # Last element as the pivot
        pivot_index = j
        # pointer store the maximun index that smaller than pivot
        pointer = i
        for idx in range(i, j):
            if array[idx] < array[pivot_index]:
                self.swap(pointer, idx)
                pointer += 1
            else:
                continue
        self.swap(pointer, j)

        return pointer

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp


array = [
    1,
    245,
    634,
    3,
    5,
    5,
    32,
    6,
    21,
    5,
    6,
    3,
    -1,
    0,
    2,
    10,
    -5,
    6,
    8,
    1020,
    33,
    9,
    7,
    14,
]

obj = QuickSort(array=array)
obj.sort()
print(obj.array)
