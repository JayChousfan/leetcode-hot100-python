"""LeetCode 338. 比特位计数 (Counting Bits) — Hot 100
难度：简单
题目：返回 0 到 n 中每个数字二进制里 1 的数量。
示例：n=5 → [0,1,1,2,1,2]
思路：用前面数字的结果推导当前答案。"""


def fun(n):
    """利用较小数字的结果计算当前数字。时间 O(n)，空间 O(n)。"""
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result


if __name__ == "__main__":
    assert fun(2) == [0, 1, 1], "示例1失败"
    assert fun(5) == [0, 1, 1, 2, 1, 2], "示例2失败"
    print("✅ E17 比特位计数 全部测试通过")
