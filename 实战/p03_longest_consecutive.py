"""
LeetCode 128. 最长连续序列 (Longest Consecutive Sequence) — ACM 实战
难度：中等

输入：第一行 n，第二行 n 个整数。
输出：最长连续序列的长度。

示例输入：
6
100 4 200 1 3 2

示例输出：
4
"""

import sys


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    nums = data[1:1 + n]
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    print(max_len)
