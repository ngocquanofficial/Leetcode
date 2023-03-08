class Solution:
    def minEatingSpeed(self, piles, h):
        # BST idea
        # Upper bound k = max(piles)
        upper = max(piles)
        lower = 1
        return self.BST(piles, h, lower, upper)


    def BST(self, piles, h, lower, upper) :
        if upper == lower :
            return upper
        mid = int((upper+lower)/2)
        time = [self.upper_natural(i/mid) for i in piles]
        total_times = int(sum(time))
        if total_times <= h :
            return self.BST(piles, h, lower, mid)
        else :
            return self.BST(piles, h, mid+1, upper)



    
    def upper_natural(self, nums) :
        if nums == int(nums) :
            return int(nums)
        else :
            return int(nums) + 1
        
piles = [3, 6, 7, 11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))