class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max, global_max = 0, 0
        buy_date, sell_date = 0, 1
        while sell_date < len(prices) and (sell_date > buy_date):
            curr_max = prices[sell_date] - prices[buy_date]
            if curr_max < global_max and prices[sell_date] < prices[buy_date]:
                buy_date = sell_date
            global_max = max(global_max, curr_max)
            sell_date += 1
        return global_max
            