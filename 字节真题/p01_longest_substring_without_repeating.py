"""LeetCode 3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters) — 字节真题
难度：中等
题目：找出字符串中不含重复字符的最长子串长度。
示例："abcabcbb" → 3
思路：滑动窗口，记录每个字符最后出现的位置。"""


def fun(s):
    """滑动窗口。时间 O(n)，空间 O(n)。"""
    char_map = {}
    left = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in char_map and char_map[ch] >= left:
            left = char_map[ch] + 1
        char_map[ch] = i
        max_len = max(max_len, i - left + 1)
    return max_len


if __name__ == "__main__":
    assert fun("abcabcbb") == 3, "示例1失败"
    assert fun("bbbbb") == 1, "重复字符测试失败"
    assert fun("") == 0, "空字符串测试失败"
    print("✅ P01 无重复字符的最长子串 全部测试通过")
