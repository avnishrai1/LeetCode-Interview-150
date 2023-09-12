class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxH = 0

        while r < len(prices) :
            if prices[l] < prices[r] :
                result = prices[r] - prices[l]
                maxH = max(result, maxH)

            else :
                l = r 

            r = r + 1

        return maxH