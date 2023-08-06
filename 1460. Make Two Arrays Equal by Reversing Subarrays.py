class Solution:
    def canBeEqual(self, target, arr):
        target_dict = dict()
        arr_dict = dict()
        for i in range(len(target)):
            # For target_dict
            if target[i] in target_dict:
                target_dict[target[i]] += 1
            else:
                target_dict[target[i]] = 1

            if arr[i] in arr_dict:
                arr_dict[arr[i]] += 1
            else:
                arr_dict[arr[i]] = 1

        if target_dict == arr_dict:
            return True
        else:
            return False
