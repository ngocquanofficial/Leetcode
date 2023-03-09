class Solution:
    def findKthPositive(self, arr, k):
        if k < arr[0] :
            return k
        else : # always missing first -1 positive integer numbers
            k = k - arr[0] + 1

        if len(arr) == 0 : # and k >= arr[0] :
            return k + 1
        

        
        # s[t] = x[t] - x[0] - t is the number of missing number up to the element t-th, except the number that <x[0]
        lower = 0
        s_lower = 0
        upper = len(arr) - 1
        s_upper = arr[upper] - arr[0] - upper
        # Special case: The k-th missing numbers is strickly larger than the arr[-1]
        if s_upper < k :
            return arr[upper] + k - s_upper
        
        
        while lower < upper :
            if lower == upper - 1 :
                return arr[lower] + k - s_lower
            mid = (lower + upper) // 2
            s_mid = arr[mid] - arr[0] - mid
            if s_mid < k :
                lower = mid
                s_lower = s_mid
            else :
                upper = mid
                s_upper = s_mid
                
            


        
arr =[1, 2, 3, 4]
k = 2
solution = Solution()
print(solution.findKthPositive(arr, k))