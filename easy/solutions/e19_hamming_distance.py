"""LeetCode 461. 汉明距离 (Hamming Distance) — Hot 100
难度：简单
题目：计算两个整数的二进制表示有多少位不同。
示例：x=1, y=4 → 2
思路：先异或，再统计结果中 1 的数量。"""


def fun(x, y):
    """统计 x ^ y 中二进制 1 的个数。时间 O(1)，空间 O(1)。"""
    return bin(x ^ y).count("1")


if __name__ == "__main__":
    assert fun(1, 4) == 2, "示例1失败"
    assert fun(3, 1) == 1, "示例2失败"
    print("✅ E19 汉明距离 全部测试通过")
