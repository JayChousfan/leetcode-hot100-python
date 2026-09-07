"""
LeetCode 49. 字母异位词分组 (Group Anagrams) — ACM 实战
难度：中等

输入：第一行 n，第二行 n 个字符串。
输出：每组异位词占一行，组内保持输入顺序。

示例输入：
6
eat tea tan ate nat bat

示例输出：
eat tea ate
tan nat
bat
"""

import sys
from collections import defaultdict


if __name__ == "__main__":
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    strs = [s.decode() for s in data[1:1 + n]]
    mp: defaultdict[str, list[str]] = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        mp[key].append(s)

    result = [" ".join(group) for group in mp.values()]
    sys.stdout.write("\n".join(result))
