class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        maxProfit = 0
        for i in prices:
            if i<min_num:
                min_num = i
            profit = i - min_num
            if profit>maxProfit:
                maxProfit = profit
        return maxProfit

