"""LeetCode 70. 爬楼梯 (Climbing Stairs) — Hot 100
难度：简单
多变量赋值可简洁滚动更新两个 DP 状态。"""


def fun(n: int) -> int:
    """滚动动态规划。时间 O(n)，空间 O(1)。"""
    prev, cur = 1, 1
    for _ in range(n):
        prev, cur = cur, prev + cur
    return prev


if __name__ == "__main__":
    assert fun(2) == 2, "示例1失败"
    assert fun(3) == 3, "示例2失败"
    print("✅ E04 爬楼梯 全部测试通过")
