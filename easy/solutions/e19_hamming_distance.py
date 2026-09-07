"""LeetCode 461. 汉明距离 (Hamming Distance) — Hot 100
难度：简单
先异或找出不同位，再用 bin().count("1") 统计二进制 1 的数量。"""


def fun(x: int, y: int) -> int:
    """统计 x ^ y 中二进制 1 的个数。时间 O(1)，空间 O(1)。"""
    return bin(x ^ y).count("1")


if __name__ == "__main__":
    assert fun(1, 4) == 2, "示例1失败"
    assert fun(3, 1) == 1, "示例2失败"
    print("✅ E19 汉明距离 全部测试通过")
