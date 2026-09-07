"""LeetCode 121. 买卖股票的最佳时机 (Best Time to Buy and Sell Stock) — Hot 100
难度：简单
题目：只能买卖股票一次，求能够获得的最大利润。
示例：[7,1,5,3,6,4] → 5
思路：遍历时维护最低价格和最大利润。"""


def fun(prices):
    """扫描最低买入价并更新最大利润。时间 O(n)，空间 O(1)。"""
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == "__main__":
    assert fun([7, 1, 5, 3, 6, 4]) == 5, "示例1失败"
    assert fun([7, 6, 4, 3, 1]) == 0, "无利润测试失败"
    print("✅ E08 买卖股票的最佳时机 全部测试通过")
