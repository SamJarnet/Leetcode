def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    min_num = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - min_num > max_profit:
            max_profit = prices[i] - min_num
        if prices[i] < min_num:
            min_num = prices[i]
    return max_profit
            

print(maxProfit([7,1,5,3,6,4]))