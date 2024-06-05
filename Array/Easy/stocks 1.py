def maxProfit(prices: list[int]) -> int:
    bp=prices[0]
    profit=0
    for sell in prices[1:]:
        if sell>bp:
            profit=max(sell-bp,profit)
        else:
            bp=sell
        print(bp,sell,profit)
    return profit

print(maxProfit([7,2,5,3,6,4,1]))