class Solution:
    def change(self, amount, coins):
        coins = sorted(coins)
        coins.insert(0, 0)
        coin_num = len(coins)
        array = [[0 for i in range(coin_num)] for j in range(amount + 1)]
        # array[b][c] means the number of combination that sum = b,
        # in the case we only use first c coins
        # Base case with c = 1
        array[0] = [1] * coin_num
        for b in range(0, amount + 1):
            # If coins[1] divided by b, then we have 1 combination
            # that contain b/coins[1] element, else we do not have
            # any combination
            if b % coins[1] == 0:
                array[b][1] = 1
            # else array[b][1] = 0, but we initialize with 0, so we do nothing

        for c in range(2, len(coins)):
            # c is the number of coin we use
            c_amount = coins[c]
            for b in range(1, amount + 1):
                # The case we use maximun max_num c-th coins
                max_num = int(b / c_amount)
                # Each element in part is the case we use exactly i c-th coins
                part = [array[b - i * c_amount][c - 1] for i in range(max_num + 1)]
                array[b][c] += sum(part)

        return array[amount][coin_num - 1]


obj = Solution()
amount = 5
coins = [1, 2, 5]
ans = obj.change(amount, coins)
print(ans)
