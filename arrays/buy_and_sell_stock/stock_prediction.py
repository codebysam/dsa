#
# Best time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# #

def get_maximum_profit_for_stock(prices):
    l = len(prices)
    i = 0
    j = 1
    max_profit = 0
    while j < l:
        print(i,j, prices[i], prices[j])
        if prices[j] > prices[i]:
            max_profit = max(max_profit, prices[j] - prices[i])
            j = j + 1
        else:
            i = j
            
    return max_profit

if __name__ == "__main__":
    print(get_maximum_profit_for_stock([7,1,5,3,6,4]))
    print(get_maximum_profit_for_stock([4,9,5,6,6,11]))