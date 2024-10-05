class BuyAndSellCrypto:

    # O(n*n)
    def sol1(self, prices: list[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > res:
                    res = profit
        return res

    # O(n)
    def sol2(self, prices: list[int]) -> int:
        res = 0
        b = 0 # buy
        s = 1 # sell
        while s < len(prices):
            p = prices[s] - prices[b] # profit
            if p > res:
                res = p
            if prices[s] < prices[b]:
                b = s
            s += 1
        return res