"""LeetCode 121. 买卖股票的最佳时机｜难度：简单
题目：只能买卖股票一次，求能够获得的最大利润。
示例：[7,1,5,3,6,4] → 5
函数：fun(prices)"""
# TODO: 在这里写出完整的 def fun(...): 函数
def fun(prices):
    min_price = float("inf")
    max_price = 0
    for price in prices:
        min_price=min(min_price,price)
        max_price=max(max_price,price-min_price)
    return max_price

if __name__ == "__main__":
    assert fun([7, 1, 5, 3, 6, 4]) == 5, "示例1失败"
    assert fun([7, 6, 4, 3, 1]) == 0, "无利润测试失败"
    print("✅ E08 买卖股票的最佳时机 通过！")
