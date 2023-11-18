class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        maxprofit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxprofit=max( maxprofit,profit)
            else:
                left=right
            right+=1
        return maxprofit
