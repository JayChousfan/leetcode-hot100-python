"""小于 N 的最大数 (Largest Number Less Than N) — 字节真题
难度：中等
题目：给定可重复使用的数字，组成小于 n 的最大非负整数。
示例：digits=[2,4,9], n=23121 → 22999
思路：从高位到低位优先选择较大数字，无法继续时回退。"""


def fun(digits, n):
    """数位搜索。时间 O(k·m)，空间 O(k)，k 为 n 的位数。"""
    digits = sorted(set(digits), reverse=True)
    limit = str(n - 1)

    def build(i, length, tight):
        if i == length:
            return ""
        max_digit = int(limit[i]) if tight else 9
        for digit in digits:
            if digit > max_digit or (i == 0 and digit == 0 and length > 1):
                continue
            suffix = build(i + 1, length, tight and digit == max_digit)
            if suffix is not None:
                return str(digit) + suffix
        return None

    for length in range(len(limit), 0, -1):
        result = build(0, length, length == len(limit))
        if result is not None:
            return int(result)
    return -1


if __name__ == "__main__":
    assert fun([2, 4, 9], 23121) == 22999, "示例1失败"
    assert fun([0, 9], 100) == 99, "缩短位数测试失败"
    print("✅ P07 小于 N 的最大数 全部测试通过")
